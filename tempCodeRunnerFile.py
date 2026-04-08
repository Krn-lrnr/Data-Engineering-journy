import pandas as pd

# -------------------------------
# STEP 1: Create sample data
# -------------------------------
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)
print("✅ CSV file created successfully!\n")


# -------------------------------
# STEP 2: Load CSV file
# -------------------------------
file_path = "data.csv"
df = pd.read_csv(file_path)

print("📄 Preview of data:")
print(df.head())


# -------------------------------
# STEP 3: Ask user for column
# -------------------------------
column = input("\nEnter column name for stats: ")


# -------------------------------
# STEP 4: Process & analyze
# -------------------------------
if column in df.columns:
    # Convert to numeric (important for safety)
    df[column] = pd.to_numeric(df[column], errors='coerce')

    # Remove missing values
    clean_data = df[column].dropna()

    # Calculate stats
    minimum = clean_data.min()
    maximum = clean_data.max()
    average = clean_data.mean()

    print("\n📊 Statistics for column:", column)
    print("Min:", minimum)
    print("Max:", maximum)
    print("Average:", average)

else:
    print("❌ Column not found in dataset.")