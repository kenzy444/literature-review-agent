.PHONY: dev test lint format export

dev:           ## Start FastAPI dev server
	poetry run uvicorn src.api.main:app --reload

test:          ## Run tests with Pytest
	poetry run pytest -q

lint:          ## Run flake8, mypy, and pre-commit checks
	poetry run flake8 src tests
	poetry run mypy src
	pre-commit run --all-files

format:        ## Reformat with black and isort
	poetry run black src tests
	poetry run isort src tests

export:        ## Export requirements.txt
	poetry export --without-hashes -f requirements.txt > deployment/requirements.txt
