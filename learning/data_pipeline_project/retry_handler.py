import requests
import time

def fetch_with_retry(url, retries=3, delay=2):

    for attempt in range(retries):

        try:
            response = requests.get(url)

            if response.status_code == 200:
                print("Data fetched successfully")
                return response.json()

            print(f"Attempt {attempt + 1} failed")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        time.sleep(delay)

    print("All retry attempts failed")
    return None