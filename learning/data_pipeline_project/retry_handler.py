import requests
import time

def fetch_with_retry(url, retries, delay):

    for attempt in range(retries):

        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()

            print(f"Attempt {attempt + 1} failed")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        time.sleep(delay)

    return None