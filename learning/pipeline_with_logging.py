import pandas as pd
import requests
import logging

# Setup logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Data extracted successfully")
        return response.json()
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None

def transform(data):
    try:
        df = pd.DataFrame(data)
        df = df[["id", "name", "email"]]
        df = df.dropna()
        logging.info("Data transformed successfully")
        return df
    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        return None

def load(df):
    try:
        df.to_csv("logged_output.csv", index=False)
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Loading failed: {e}")

def pipeline():
    data = extract()
    if data:
        df = transform(data)
        if df is not None:
            load(df)
        else:
            logging.error("Pipeline stopped at transform stage")
    else:
        logging.error("Pipeline stopped at extract stage")

if __name__ == "__main__":
    pipeline()