import re


def remove_parentheses_text(input_file, output_file):
    # Read the song titles from the input file
    with open(input_file, 'r') as file:
        song_titles = file.read().strip().split('\n')

    # Remove text in parentheses from each title and strip trailing spaces
    cleaned_titles = [re.sub(r'\s*\(.*?\)\s*', '', title).strip()
                      for title in song_titles]

    # Write the cleaned titles to the output file without adding extra spaces or new lines
    with open(output_file, 'w') as file:
        for title in cleaned_titles:
            if title:  # Only write non-empty titles
                file.write(title + '\n')


# Specify the input and output files
input_file = 'input.txt'
output_file = 'output.txt'

# Process the song titles and write to the output file
remove_parentheses_text(input_file, output_file)
