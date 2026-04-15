import pandas as pd

file_path = "data.csv"

try:
    df = pd.read_csv(file_path)

    print("Original Data:")
    print(df)

    filtered_df = df[df["salary"] > 55000]

    print("\nFiltered Data (salary > 55000):")
    print(filtered_df)
   
    filtered_df.to_csv("filtered_data.csv", index=False)

    print("\nFiltered data saved to filtered_data.csv")

except FileNotFoundError:
    print("File not found. Please check the file path.")