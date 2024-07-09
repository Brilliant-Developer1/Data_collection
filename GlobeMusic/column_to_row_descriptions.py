def read_file(file_path):
    # Read the file and remove empty lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines

def convert_column_to_row(data):
    # Join all descriptions into a single string separated by tab
    return '\t'.join(data)

def save_to_file(data, file_path):
    # Save the data to a text file
    with open(file_path, 'w') as file:
        file.write(data)

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file and clean the data
    data = read_file(input_file)

    # Convert the column to a row
    row_data = convert_column_to_row(data)

    # Save the row to the output file
    save_to_file(row_data, output_file)

    print(f'Column data has been converted to row and saved to {output_file}')

if __name__ == "__main__":
    main()
