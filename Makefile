lint: 
	uv run ruff check .
	uv run black --check .

format:
	uv run ruff check . --fix
	uv run black .

install:
	uv sync --all-groups

install-prod:
	uv sync

run:
	uv run uvicorn src.main:app --port=3000 --reload

debug:
	DEBUG=true uv run uvicorn src.main:app --port=3000 --reload --log-level debug

test:
	uv run pytest

exp-requirements:
	uv export --format requirements.txt



