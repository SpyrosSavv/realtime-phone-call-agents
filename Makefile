ifeq (,$(wildcard .env))
$(error .env file is missing. Please create one based on .env.example)
endif

include .env

CHECK_DIRS := src/

# Ruff

format-fix:
	uv run ruff format $(CHECK_DIRS) 
	uv run ruff check --select I --fix

lint-fix:
	uv run ruff check --fix $(CHECK_DIRS) 

format-check:
	uv run ruff format --check $(CHECK_DIRS) 
	uv run ruff check -e $(CHECK_DIRS)
	uv run ruff check --select I -e

lint-check:
	uv run ruff check $(CHECK_DIRS)

# Run Gradio app

start-gradio-application:
	uv run python scripts/run_gradio_application.py

# Application Local Deployment

start-call-center:
	docker compose up -d

stop-call-center:
	docker compose down