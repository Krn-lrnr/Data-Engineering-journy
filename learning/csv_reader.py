import pandas as pd

# This block is a sample data set
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# This one turns dataframe into csv
df.to_csv("data.csv", index=False)
print("✅ CSV file created successfully!\n")


# This one loades the csv file
file_path = "data.csv"
df = pd.read_csv(file_path)

print("📄 Preview of data:")
print(df.head())


# Asking for input
column = input("\nEnter column name for stats: ")


# Processinga and analyzing-
if column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        clean_data = df[column].dropna()

        print("\n📊 Statistics for column:", column)
        print("Min:", clean_data.min())
        print("Max:", clean_data.max())
        print("Average:", clean_data.mean())
    else:
        print("❌ Selected column is not numeric.")
        print("Please choose a numeric column like:", list(df.select_dtypes(include='number').columns))
else:
    print("❌ Column not found.")
    print("Available columns:", list(df.columns))