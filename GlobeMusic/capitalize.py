def read_file(file_path):
    # Read the file into a list of lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def capitalize_titles(lines):
    # Capitalize the first letter of each word in each line
    return [line.title() for line in lines]

def save_to_file(data, file_path):
    # Save the data to a text file
    with open(file_path, 'w') as file:
        file.writelines(data)

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input2.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file
    lines = read_file(input_file)

    # Capitalize the titles
    capitalized_titles = capitalize_titles(lines)

    # Save the capitalized titles to the output file
    save_to_file(capitalized_titles, output_file)

    print(f'The titles have been capitalized and saved to {output_file}')

if __name__ == "__main__":
    main()
