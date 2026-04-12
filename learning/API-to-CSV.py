import requests
import pandas as pd

# API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# Data fetch
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # JSON to DataFrame
    df = pd.DataFrame(data)

    # columns selection
    df = df[["id", "name", "username", "email", "phone", "website"]]

    # Save to CSV
    df.to_csv("users_data.csv", index=False)

    print("Data fetched and saved to users_data.csv")
else:
    print("Failed to fetch data")