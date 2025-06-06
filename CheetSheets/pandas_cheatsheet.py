import pandas as pd

# -------- Creating DataFrames --------
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
# Create a DataFrame from dictionary data

# -------- Reading and Writing --------
df.to_csv('data.csv', index=False)
# Save DataFrame to CSV file without index

df_from_csv = pd.read_csv('data.csv')
# Read DataFrame from CSV file

# -------- Basic DataFrame Info --------
df.head()
# Show first 5 rows

df.tail()
# Show last 5 rows

df.info()
# Summary including data types and memory usage

df.describe()
# Statistical summary (mean, std, min, max, quartiles) for numeric columns

# -------- Selection and Indexing --------
df['Age']
# Select a single column (returns a Series)

df[['Name', 'Age']]
# Select multiple columns (returns a DataFrame)

df.iloc[0]
# Select first row by integer location

df.loc[0]
# Select first row by index label (same here as index 0)

# -------- Filtering --------
df[df['Age'] > 26]
# Filter rows where Age is greater than 26

# -------- Modifying Data --------
df['Age'] = df['Age'] + 1
# Add 1 to every Age value

df['NewCol'] = [100, 200]
# Add new column with values

# -------- Handling Missing Data --------
df.dropna()
# Drop rows with any NaN values

df.fillna(0)
# Fill all NaN values with 0

# -------- Grouping and Aggregating --------
grouped = df.groupby('Name').mean()
# Group by 'Name' and compute mean of other columns

# -------- Sorting --------
df.sort_values('Age')
# Sort DataFrame by Age in ascending order

# -------- Merging and Joining --------
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})
merged = pd.merge(df1, df2, on='ID')
# Merge two DataFrames on column 'ID'

# -------- Time Series --------
dates = pd.date_range('2023-01-01', periods=6)
ts_df = pd.DataFrame({'Date': dates, 'Value': range(6)})
ts_df.set_index('Date', inplace=True)
# Set Date column as index (for time series analysis)
