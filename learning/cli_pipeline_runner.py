import argparse
import pandas as pd

def process(input_file, output_file):
    df = pd.read_csv(input_file)

    # basic cleaning
    df = df.dropna()
    df.columns = df.columns.str.lower()

    # example filter
    if "salary" in df.columns:
        df = df[df["salary"] > 50000]

    df.to_csv(output_file, index=False)
    print("Processing completed")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")

    args = parser.parse_args()

    process(args.input, args.output)

if __name__ == "__main__":
    main()