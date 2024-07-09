def read_file(file_path):
    # Read the file into a list of lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def reverse_lines(lines):
    # Reverse the order of the lines
    return lines[::-1]

def save_to_file(data, file_path):
    # Save the data to a text file
    with open(file_path, 'w') as file:
        file.writelines(data)

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file
    lines = read_file(input_file)

    # Reverse the lines
    reversed_lines = reverse_lines(lines)

    # Save the reversed lines to the output file
    save_to_file(reversed_lines, output_file)

    print(f'The data has been reversed and saved to {output_file}')

if __name__ == "__main__":
    main()
