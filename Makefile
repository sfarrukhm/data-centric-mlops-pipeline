# Default values
year ?= 2025
month ?= 04

# Ingest data
ingest-data:
	uv run python src/data/ingest.py -y $(year) -m $(month)

# Clean data
clean-data:
	uv run python src/data/clean.py -y $(year) -m $(month)

# Run both ingest and clean
ingest-clean: ingest-data clean-data

dvc:
	uv run dvc add data/processed/green_tripdata_$(year)-$(month)-cleaned.parquet
	git add data/processed/green_tripdata_$(year)-$(month)-cleaned.parquet.dvc
	git commit -m "Add data: year $(year), month $(month)"
# 	uv run dvc push

all: ingest-data clean-data dvc