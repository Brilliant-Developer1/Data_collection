def read_file(file_path):
    # Read the file and remove empty lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines

def save_to_file(data, file_path):
    # Save the cleaned data to a text file
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file and clean the data
    cleaned_data = read_file(input_file)

    # Save the cleaned data to the output file
    save_to_file(cleaned_data, output_file)

    print(f'Empty cells have been removed and cleaned data has been saved to {output_file}')

if __name__ == "__main__":
    main()
