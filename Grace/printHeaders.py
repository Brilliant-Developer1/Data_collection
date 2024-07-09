import pandas as pd

# Load the CSV data
data = pd.read_csv('Data.csv')

# Print the headers to check column names
print(data.columns)
