import os
import requests
from datetime import datetime
from pathlib import Path
import logging
import argparse


SCRIPT_DIR=Path(__file__).resolve().parent

base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
data_type = "green_tripdata"
raw_data_dir=SCRIPT_DIR.parent /"data"/"raw"
log_path=SCRIPT_DIR.parent /"logs"/"app.log"
# add logging
# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# File handler
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# stream (console) handler
console_handler=logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)



def download_month(year:int, month:int):
    """Downloads a specific month of green taxi data."""

    raw_data_dir.mkdir(parents=True, exist_ok=True)
    file_name=f"{data_type}_{year}-{month:02d}.parquet"
    url=f"{base_url}/{file_name}"

    dest_path=raw_data_dir/file_name

    if dest_path.exists():
        logger.info(f"File {dest_path} already exists. Skipping download.")
        return dest_path
    logger.info(f"Downloading {file_name} ...")
    resp=requests.get(url)

    if resp.status_code==200:
        with open(dest_path,"wb") as f:
            f.write(resp.content)
        logger.info(f"Downloaded {file_name}")
        return dest_path
    else:
        logger.info(f"Failed to download {file_name} (status {resp.status_code})")

def main(year, month):
    download_month(year, month)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Arguments for downloading data")
    parser.add_argument("-y","--year",type=int,help="Which year?")
    parser.add_argument("-m","--month",type=int, help="Which month? (1-12)")
    args=parser.parse_args()

    main(args.year, args.month)
