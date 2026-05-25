import os

def load_config():
    return {
        "url": os.getenv("API_URL"),
        "output_file": os.getenv("OUTPUT_FILE")
    }