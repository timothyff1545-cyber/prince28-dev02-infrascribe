"""App factory: build a fully wired FastAPI app from settings."""

import json
import logging
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from infrascribe.api.errors import register_error_handlers
from infrascribe.api.middleware import request_context
from infrascribe.api.routes import documents, health
from infrascribe.config import Settings, get_settings
from infrascribe.logging_setup import setup_logging
from infrascribe.store import RecordStore

logger = logging.getLogger("infrascribe")


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    setup_logging(settings.log_level)
    store = RecordStore(settings.data_file)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        try:
            count = store.load()
            logger.info("records loaded", extra={"records": count})
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            logger.error("could not load records: %s", exc)
        yield

    app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
    app.state.settings = settings
    app.state.store = store

    app.middleware("http")(request_context)
    register_error_handlers(app)

    v1 = APIRouter(prefix="/v1")
    v1.include_router(documents.router)
    app.include_router(health.router)
    app.include_router(v1)
    return app
