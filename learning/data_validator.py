import pandas as pd

file_path = "data.csv"

try:
    df = pd.read_csv(file_path)

    print("Data Validation Report\n")

    # Check missing values
    print("Missing values per column:")
    print(df.isnull().sum())
    print()

    # Check duplicates
    duplicate_count = df.duplicated().sum()
    print("Duplicate rows:", duplicate_count)
    print()

    # Check numeric columns for negative values
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        negatives = (df[col] < 0).sum()
        if negatives > 0:
            print(f"Column '{col}' has {negatives} negative values")

    print()

    # Check data types
    print("Column data types:")
    print(df.dtypes)

except FileNotFoundError:
    print("File not found")