import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    df = df[["id", "name", "email", "phone", "website"]]

    df.columns = df.columns.str.strip().str.lower()

    df["email"] = df["email"].str.lower()

    df = df.drop_duplicates()

    df = df[df["name"].notna()]

    df.to_csv("clean_users.csv", index=False)

    print("Cleaned data saved to clean_users.csv")
else:
    print("Failed to fetch data")