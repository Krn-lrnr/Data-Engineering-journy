import pandas as pd

file_path = "data.csv"

try:
    df = pd.read_csv(file_path)

    print("\nDataset Summary\n")

    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])

    print("\nColumns:")
    print(list(df.columns))

    print("\nData Types:")
    print(df.dtypes)

    print("\nNumeric Summary:")
    print(df.describe())

except FileNotFoundError:
    print("File not found. Please check the file path.")