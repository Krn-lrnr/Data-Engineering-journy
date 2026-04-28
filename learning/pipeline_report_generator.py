import pandas as pd

input_file = "data.csv"
report_file = "report.txt"

try:
    df = pd.read_csv(input_file)

    with open(report_file, "w") as f:
        f.write("DATA REPORT\n\n")

        f.write(f"Rows: {df.shape[0]}\n")
        f.write(f"Columns: {df.shape[1]}\n\n")

        f.write("Column Names:\n")
        f.write(str(list(df.columns)) + "\n\n")

        f.write("Missing Values:\n")
        f.write(str(df.isnull().sum()) + "\n\n")

        f.write("Data Types:\n")
        f.write(str(df.dtypes) + "\n\n")

        f.write("Numeric Summary:\n")
        f.write(str(df.describe()) + "\n")

    print("Report generated successfully")

except FileNotFoundError:
    print("Input file not found")