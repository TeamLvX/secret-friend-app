lint: 
	uv run ruff check .
	uv run black --check .

format:
	uv run ruff check . --fix
	uv run black .

install:
	uv sync --all-groups

install-prod:
	uv sync --frozen
	uv cache prune --ci

initialize:
	docker compose up

build-image:
	docker build -t $(APP_NAME) .

docker-run:
	docker run -p $(PORT):3000 --network $(APP_NAME)_default --env-file .env -e DYNAMODB_ENDPOINT=http://localstack:4566 --name $(APP_NAME) $(APP_NAME)

deploy:
	terraform apply -auto-approve

destroy:
	terraform destroy -auto-approve

run:
	uv run uvicorn src.main:app --port=3000 --reload

run-prod:
	uv run uvicorn src.main:app --host 0.0.0.0 --port $(PORT)

run-cloudflared:
	cloudflared tunnel --url http://127.0.0.1:3000

debug:
	DEBUG=true uv run uvicorn src.main:app --port=3000 --reload --log-level debug

test:
	uv run pytest

exp-requirements:
	uv export --format requirements.txt



