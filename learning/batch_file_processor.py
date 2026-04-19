import pandas as pd
import os

folder_path = "data_files"
output_file = "combined_data.csv"

all_data = []

try:
    files = os.listdir(folder_path)

    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)

            # Clean column names
            df.columns = df.columns.str.strip().str.lower()

            # Drop missing values
            df = df.dropna()

            all_data.append(df)

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_csv(output_file, index=False)
        print("All files processed and combined successfully")
    else:
        print("No CSV files found")

except FileNotFoundError:
    print("Folder not found")