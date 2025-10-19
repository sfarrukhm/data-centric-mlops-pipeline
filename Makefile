PYTHON := python
# Path to your script
INGEST_SCRIPT := scripts/data_ingestion.py

install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint-format:
	ruff check . && ruff format .

# data ingest
year ?=2025
month ?=04

data-ingest:
	$(PYTHON) $(INGEST_SCRIPT) -y $(year) -m $(month)
