import json
from extract import extract
from transform import transform
from load import load

def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    data = extract(config["url"])

    if data:
        df = transform(data)
        load(df, config["output_file"])
        print("Pipeline executed successfully")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    main()