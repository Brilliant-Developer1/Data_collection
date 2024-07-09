# Define the paths to the input and output files
input_file_path = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
output_file_path = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

# Read the codes from the input file
with open(input_file_path, 'r') as file:
    codes = [line.strip() for line in file if line.strip()]

# Write the codes to the output file 88 times each
with open(output_file_path, 'w') as file:
    for code in codes:
        for _ in range(88):
            file.write(code + '\n')
