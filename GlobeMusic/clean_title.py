import re

def clean_title(title):
    # Remove '-' and "'"
    title = title.replace('-', ' ').replace("'", "").replace("&", "").replace("(", "").replace(")", "").replace("up", "").replace("Up", "").replace("  ", " ").replace("Sample", "").replace("Samples", "").replace("Loop", "")

    # Remove words starting with a small letter
    title = ' '.join(word for word in title.split() if not word[0].islower())

    roman_numerals = re.compile(r'\b[IVXLCDM]+\b', re.IGNORECASE)
    title = roman_numerals.sub('', title).strip()

    # Ensure no double spaces
    title = re.sub(' +', ' ', title)
    return title


def process_titles(input_file, output_file):
    with open(input_file, 'r') as infile:
        titles = infile.readlines()
    
    cleaned_titles = [clean_title(title.strip()) for title in titles]
    
    with open(output_file, 'w') as outfile:
        for title in cleaned_titles:
            outfile.write(title + '\n')

# File names
input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

# Process the titles
process_titles(input_file, output_file)

print("Titles cleaned and written to output.txt")
