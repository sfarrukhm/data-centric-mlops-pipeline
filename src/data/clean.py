"""
clean_data.py
-------------
Reads raw NYC Green Taxi data (2025-01),
cleans it, and saves a processed version.
"""

import pandas as pd
import numpy as np
import os
import argparse

# ---------- Configuration ----------
RAW_DATA_PATH = "data/raw/green_tripdata_2025-01.parquet"
PROCESSED_DATA_PATH = "data/processed/green_tripdata_2025-01-cleaned.parquet"


def load_data(path: str) -> pd.DataFrame:
    """Load parquet file into pandas DataFrame."""
    print(f"📥 Loading data from {path} ...")
    df = pd.read_parquet(path)
    print(f"✅ Loaded successfully. Shape: {df.shape}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the NYC Green Taxi dataset."""
    print("🧹 Starting cleaning process...")

    # 1️⃣ Drop columns that are completely empty or useless
    drop_cols = ["ehail_fee"]  # all nulls
    df = df.drop(columns=drop_cols, errors="ignore")

    # 2️⃣ Handle missing values — these columns have nulls
    fill_zero = ["passenger_count", "RatecodeID", "payment_type", "trip_type"]
    for col in fill_zero:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # 3️⃣ Fix data types
    int_cols = ["RatecodeID", "payment_type", "trip_type"]
    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].astype("int32")

    # 4️⃣ Remove invalid trips
    df = df[(df["trip_distance"] > 0) & (df["fare_amount"] > 0)]

    # 5️⃣ Compute trip duration in minutes
    df["trip_duration_min"] = (
        (df["lpep_dropoff_datetime"] - df["lpep_pickup_datetime"])
        .dt.total_seconds()
        / 60
    )

    # 6️⃣ Filter unreasonable durations (>6 hours)
    df = df[df["trip_duration_min"] <= 360]

    # 7️⃣ Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"🔁 Removed {before - after} duplicates.")

    # 8️⃣ Optional: handle outliers for fare and distance
    df = df[df["fare_amount"] < df["fare_amount"].quantile(0.99)]
    df = df[df["trip_distance"] < df["trip_distance"].quantile(0.99)]

    # 9️⃣ Final sanity checks
    print(f"✅ Cleaned dataset shape: {df.shape}")
    print(f"🧾 Columns: {list(df.columns)}")

    return df


def save_data(df: pd.DataFrame, path: str):
    """Save cleaned data."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"💾 Saved cleaned data to {path}")


def main(year:int, month:int):
    RAW_DATA_PATH = f"data/raw/green_tripdata_{year}-{month:02d}.parquet"
    PROCESSED_DATA_PATH = f"data/processed/green_tripdata_{year}-{month:02d}-cleaned.parquet"

    df = load_data(RAW_DATA_PATH)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, PROCESSED_DATA_PATH)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean NYC Green Taxi data.")
    parser.add_argument("-y","--year", type=int, default=2025, help="Year of the data to clean.")
    parser.add_argument("-m","--month", type=int, default=1, help="Month of the data to clean.")
    args = parser.parse_args()
    main(args.year, args.month)
    