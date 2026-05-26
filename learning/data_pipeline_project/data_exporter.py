import pandas as pd

def export_csv(df, filename):
    df.to_csv(filename, index=False)

def export_json(df, filename):
    df.to_json(filename, orient="records", indent=4)

def export_excel(df, filename):
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    print("Exporter module loaded")