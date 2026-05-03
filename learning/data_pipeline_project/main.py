import json
import logging
try:
    from extract import extract
    from transform import transform
    from load import load
except ImportError as e:
    logging.error(f"Failed to import modules: {e}")
    raise

# setup logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)

        logging.info("Config loaded")

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