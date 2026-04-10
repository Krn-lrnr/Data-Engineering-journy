import pandas as pd

# database loaded

file_path = "data.csv"   
df = pd.read_csv(file_path)

print("\n📄 Original Data:")
print(df)

# duplicate rows deleted

df = df.drop_duplicates()
print("\n✅ Removed duplicates")

# filled missing values

for col in df.select_dtypes(include='number').columns:
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col].fillna("Unknown", inplace=True)

print("✅ Handled missing values")

#colum name cleaned

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("✅ Cleaned column names")

# outlier removed

for col in df.select_dtypes(include='number').columns:
    df = df[df[col] < df[col].quantile(0.99)]

print("✅ Removed extreme outliers")

# clean data saved
output_file = "cleaned_data.csv"
df.to_csv(output_file, index=False)

print("\n🎯 Cleaned data saved as:", output_file)
print("\n📊 Final Data:")
print(df.head())