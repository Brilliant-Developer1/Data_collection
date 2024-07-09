import pandas as pd

# Read the input files
input_file1 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
input_file2 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input2.txt'

# Read the data from input.txt
df1 = pd.read_csv(input_file1, sep='\t')

# Read the data from input2.txt
df2 = pd.read_csv(input_file2, sep='\t')

# Find the tracks in df1 that are not in df2
result_df = df1[~df1['Track ISRC'].isin(df2['Track ISRC'])]

# Write the result to output.txt
output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'
result_df.to_csv(output_file, sep='\t', index=False)

print("Duplicates removed and output written to output.txt")
