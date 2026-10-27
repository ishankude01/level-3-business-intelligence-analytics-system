
import pandas as pd
import sqlite3

# Extract data
df = pd.read_csv("SampleSuperstore.csv")
print("Original rows:", len(df))

# Transform data
df.columns = df.columns.str.strip()
df = df.drop_duplicates()

for col in ["Sales", "Quantity", "Discount", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(
    subset=["Sales", "Quantity", "Discount", "Profit"]
)

print("Cleaned rows:", len(df))

# Load cleaned data into SQLite
conn = sqlite3.connect("Business_Intelligence.db")
df.to_sql("sales_cleaned", conn, if_exists="replace", index=False)
conn.close()

print("ETL pipeline completed successfully.")
