import pandas as pd

def profile_data(file_path):

    df = pd.read_csv(file_path)

    print("\nDATA PROFILE")
    print("-" * 30)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names:")
    print(list(df.columns))

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

if __name__ == "__main__":
    profile_data("data.csv")