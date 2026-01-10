lint: 
	ruff check .
	black --check .

format:
	ruff check . --fix
	black .

install:
	pip install -r requirements.txt

run:
    docker compose up -d && uvicorn src.main:app --port=3000 --reload



