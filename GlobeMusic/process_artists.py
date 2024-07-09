# Define the paths to the input and output files
input_file_path = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
output_file_path = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

# Read the artist names from the input file
with open(input_file_path, 'r') as file:
    artist_names = file.readlines()

# Remove duplicates and strip any leading/trailing whitespace characters
unique_artist_names = sorted(set(name.strip()
                             for name in artist_names if name.strip()))

# Write the unique artist names to the output file
with open(output_file_path, 'w') as file:
    for name in unique_artist_names:
        file.write(name + '\n')
