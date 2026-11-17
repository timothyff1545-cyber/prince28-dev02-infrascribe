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
