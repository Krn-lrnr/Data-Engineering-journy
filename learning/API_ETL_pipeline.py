import requests
import pandas as pd

def extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def transform(data):
    df = pd.DataFrame(data)

    # Select useful columns
    df = df[["id", "name", "email", "phone", "website"]]

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    return df

def load(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    url = "https://jsonplaceholder.typicode.com/users"
    output_file = "api_processed_data.csv"

    data = extract(url)

    if data:
        df = transform(data)
        load(df, output_file)
        print("API ETL pipeline completed successfully")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    main()