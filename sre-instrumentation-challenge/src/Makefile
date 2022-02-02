.PHONY: dev prod watch lint test run

dev:
	pip3 install -e .[dev]

prod:
	pip3 install -e .

watch:
	hupper -m waitress --port 5000 storage:app

lint:
	mypy storage/

test:
	pytest storage/test.py

run:
	python3 run.py
