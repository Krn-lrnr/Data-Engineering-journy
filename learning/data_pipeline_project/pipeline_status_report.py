import pandas as pd

def generate_report(df, output_file):
    print("\nPIPELINE STATUS REPORT")
    print("-" * 30)

    print(f"Rows processed: {len(df)}")
    print(f"Columns processed: {len(df.columns)}")

    print("\nColumn names:")
    for column in df.columns:
        print(f"- {column}")

    print(f"\nOutput file: {output_file}")

    print("\nPipeline completed successfully")