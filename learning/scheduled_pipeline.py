import time
import pandas as pd
import requests

def extract():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def transform(data):
    df = pd.DataFrame(data)
    df = df[["id", "name", "email"]]
    df = df.dropna()
    return df

def load(df):
    df.to_csv("scheduled_output.csv", index=False)

def pipeline():
    data = extract()
    if data:
        df = transform(data)
        load(df)
        print("Pipeline run completed")
    else:
        print("Failed to fetch data")

def main():
    while True:
        pipeline()
        print("Waiting for next run...\n")
        time.sleep(10)  # runs every 10 seconds (for demo)

if __name__ == "__main__":
    main()