import json
import logging
import argparse
from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--config", default="config.json", help="Path to config file")
    parser.add_argument("--output", help="Override output file")

    args = parser.parse_args()

    try:
        with open(args.config, "r") as f:
            config = json.load(f)

        logging.info("Config loaded")

        if args.output:
            config["output_file"] = args.output

        data = extract(config["url"])

        if data:
            logging.info("Data extracted")

            df = transform(data)
            logging.info("Data transformed")

            load(df, config["output_file"])
            logging.info("Data loaded successfully")

            print("Pipeline executed successfully")

        else:
            logging.error("Extraction failed")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()