import pandas as pd
import requests
import json

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def transform(data, columns):
    df = pd.DataFrame(data)
    df = df[columns]
    df = df.dropna()
    return df

def load(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    config = load_config()

    data = extract(config["url"])

    if data:
        df = transform(data, config["columns"])
        load(df, config["output_file"])
        print("Pipeline ran using config successfully")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    main()
    