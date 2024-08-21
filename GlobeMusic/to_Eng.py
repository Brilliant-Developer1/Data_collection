import unidecode

def read_file(file_path):
    # Read the file into a list of lines
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def clean_titles(titles):
    # Replace non-English characters with their closest English equivalents
    return [unidecode.unidecode(title) for title in titles]

def save_to_file(data, file_path):
    # Save the data to a text file
    with open(file_path, 'w', encoding='utf-8') as file:
        for title in data:
            file.write(title + '\n')

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file
    titles = read_file(input_file)

    # Clean the titles
    cleaned_titles = clean_titles(titles)

    # Save the cleaned titles to the output file
    save_to_file(cleaned_titles, output_file)

    print('Non-English characters have been replaced and saved to output.txt')

if __name__ == "__main__":
    main()
