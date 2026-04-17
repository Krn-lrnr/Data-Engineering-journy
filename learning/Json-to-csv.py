import json
import pandas as pd

input_file = "data.json"
output_file = "converted_data.csv"

try:
    with open(input_file, "r") as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    df.to_csv(output_file, index=False)

    print("JSON converted to CSV successfully")

except FileNotFoundError:
    print("JSON file not found")