import pandas as pd

def extract(file_path):
    return pd.read_csv(file_path)

def transform(df):
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Drop duplicates
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna()

    # Filter condition
    df = df[df["salary"] > 50000]

    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    file_path = "data.csv"
    output_path = "processed_data.csv"

    try:
        df = extract(file_path)
        df = transform(df)
        load(df, output_path)

        print("ETL pipeline completed. Output saved to processed_data.csv")

    except FileNotFoundError:
        print("File not found. Check file path.")

if __name__ == "__main__":
    main()