lint: 
	ruff check .
	black --check .

format:
	ruff check . --fix
	black .