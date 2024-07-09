# Define the path to the output file
output_file_path = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as file:
    for _ in range(115):
        for number in range(1, 11):
            file.write(f"{number}\n")

print("Numbers 1 to 10 have been written 115 times to output.txt")
