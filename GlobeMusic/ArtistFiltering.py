import pandas as pd

# Read the input files
input_file1 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
input_file2 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input2.txt'

# Read the data from input.txt
df1 = pd.read_csv(input_file1, sep='\t')

# Read the data from input2.txt
df2 = pd.read_csv(input_file2, sep='\t')

# Filter the matched artists
matched_df = df1[df1['Artist Name'].isin(df2['Artist Name'])]

# Replace NaN values or empty strings with 'request'
matched_df['Spotify Artist ID'].replace('', 'request', inplace=True)
matched_df['Apple Music ID'].replace('', 'request', inplace=True)

# Additionally, ensure to replace NaN values with 'request'
matched_df['Spotify Artist ID'].fillna('request', inplace=True)
matched_df['Apple Music ID'].fillna('request', inplace=True)

# Write the result to output.txt
output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'
matched_df.to_csv(output_file, sep='\t', index=False)

print("Matched artist details written to output.txt")
