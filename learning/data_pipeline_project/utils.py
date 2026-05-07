import logging
import pandas as pd

def setup_logger():
    logging.basicConfig(
        filename="pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

def remove_missing(df):
    return df.dropna()

def save_csv(df, output_file):
    df.to_csv(output_file, index=False)