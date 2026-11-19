# InfraScribe

A Terraform assistant for AWS that answers resource and argument questions from the provider docs and returns HCL that passes validation.

**Status:** Day 1 foundation (FastAPI skeleton, quality gates). Live URL from Day 5.

## Who it's for

DevOps engineer at a Chennai fintech moving from manual console work to Terraform.

## The problem

The AWS provider has 1,500+ resource pages and major versions change arguments. Copied snippets often fail 'terraform validate'.

## Data sources

terraform-provider-aws website/docs (resources and data sources), CHANGELOG and version upgrade guides.

- https://github.com/hashicorp/terraform-provider-aws
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs
- Terms: Provider docs are MPL-2.0 in the repository.

## Hardest problem (my interview story)

Provider major versions rename or remove arguments; answers must match the user's pinned version, and every generated HCL snippet must pass terraform fmt and validate in a sandbox before it is shown.

## Signature feature

Validated snippets: each HCL answer shows a green 'validate passed' badge or the exact error.

## Target metric

90%+ of generated snippets pass terraform validate on 40 tasks.

## Run it locally

```bash
uv sync
cp .env.example .env   # Windows: copy .env.example .env
uv run uvicorn infrascribe.api.main:create_app --factory --reload
```

Then open http://localhost:8000/docs

## Checks

```bash
uv run pytest
uv run ruff check .
```
## Run locally in one command

You need Docker Desktop running. From a fresh clone:

```bash
docker compose up --build
```

This starts Postgres (with pgvector), Redis, runs the migrations and loads the sample data once, then starts the API.

- API docs: http://localhost:8000/docs
- Liveness: http://localhost:8000/health
- Readiness (checks the database): http://localhost:8000/ready

Stop with `Ctrl+C`, then `docker compose down`. Add `-v` to also delete the database volume.

## Develop and test

| Task | Mac / Linux | Windows |
|---|---|---|
| Run the API with reload | `make dev` | `uv run poe dev` |
| Unit tests (no network) | `make test` | `uv run poe test` |
| Integration tests (needs `docker compose up`) | `make test-integration` | `uv run poe test-integration` |
| Coverage report | `make cov` | `uv run poe cov` |
| Lint and format check | `make lint` | `uv run poe lint` |


## D04 · Docker, Compose and tests

### The image

```text
the output of: docker images infrascribe:dev

IMAGE             ID             DISK USAGE   CONTENT SIZE   EXTRA
infrascribe:dev   7e4ef93ee1d0        439MB          105MB

the output of: docker run --rm infrascribe:dev id
:dev id
uid=999(app) gid=999(app) groups=999(app)
```

- Size: 439 MB (target: under 400 MB)
- First build: 60.7 s. After changing one line of code: 23.6 s.
- Which step said CACHED, and why? (1 line, your own words)
The dependency installation step was cached because the dependency files had not changed. Docker reused the previously created layer instead of reinstalling the dependencies, which reduced the rebuild time.


### The stack

```text
the output of: docker compose ps -a

NAME                    IMAGE                    COMMAND                  SERVICE   CREATED         STATUS                 PORTS
infrascribe-api-1       infrascribe-api          "sh -c 'exec uvicorn…"   api       5 minutes ago   Up 4 minutes (healthy)     0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp
infrascribe-db-1        pgvector/pgvector:pg17   "docker-entrypoint.s…"   db        5 minutes ago   Up 4 minutes (healthy)     0.0.0.0:5433->5432/tcp, [::]:5433->5432/tcp
infrascribe-migrate-1   infrascribe-migrate      "sh -c 'alembic upgr…"   migrate   5 minutes ago   Exited (0) 4 minutes ago
infrascribe-redis-1     redis:7-alpine           "docker-entrypoint.s…"   redis     5 minutes ago   Up 4 minutes (healthy)     0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp

the last line of: docker compose logs migrate   (first up, then after down + up)
migrate-1  | records=3 inserted=3 updated=0 unchanged=0

```

### Breaking the database on purpose

```text
db stopped:  /health → {"status":"ok","app":"infrascribe","env":"local"}
db stopped:  /ready  → {"status":"not_ready","checks":{"database":false}}
db started:  /ready  → {"status":"ready","checks":{"database":true}}
```

Why should a load balancer stop sending traffic here but not restart the app? (2 lines)

A load balancer should stop sending traffic to the app when /ready returns not_ready because the application cannot safely handle requests.it should not restart the app, because the app process itself is still alive—/health returns status: ok.

### Tests and coverage

```text
uv run poe test              → 16 passed in 0.30s
uv run poe test-integration  → 7 passed in 3.54s
coverage TOTAL, unit only    → 73%
coverage TOTAL, with integration tests → 81%
```
Two files or lines my coverage report says are never run, and whether they matter: (2 lines)
- main.py — Startup code may not be covered because tests don't launch the application normally. It still matters for production startup.
- seed.py — Database seeding code may not run during tests, but it matters when initializing the database with initial data.
