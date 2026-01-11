lint: 
	ruff check .
	black --check .

format:
	ruff check . --fix
	black .

install:
	pip install -r requirements.txt

run:
	uvicorn src.main:app --port=3000 --reload



