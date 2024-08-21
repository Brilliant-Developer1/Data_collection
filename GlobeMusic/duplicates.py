import random

def read_file(file_path):
    # Read the file into a list of lines
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def replace_duplicates(titles):
    # Words to replace duplicates
    replacements = ['Tune', 'Sound', 'Tunes', 'Sounds', 'Dreams', 'Night']
    seen = {}
    duplicate_count = 0

    for i in range(len(titles)):
        if titles[i] in seen:
            duplicate_count += 1
            # Split the title and replace the last word
            parts = titles[i].split()
            if len(parts) > 1:
                parts[-1] = random.choice(replacements)
            else:
                parts.append(random.choice(replacements))
            titles[i] = ' '.join(parts)
        seen[titles[i]] = seen.get(titles[i], 0) + 1

    return titles, duplicate_count

def process_chunks(titles, chunk_size):
    # Process titles in chunks
    chunks = [titles[i:i + chunk_size] for i in range(0, len(titles), chunk_size)]
    total_duplicates = 0

    with open('/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt', 'w') as outfile:
        for chunk in chunks:
            updated_chunk, duplicates = replace_duplicates(chunk)
            total_duplicates += duplicates
            outfile.write('\n'.join(updated_chunk) + '\n')

    return total_duplicates

def main():
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    chunk_size = 40

    titles = read_file(input_file)
    total_duplicates = process_chunks(titles, chunk_size)

    print(f'Total duplicates: {total_duplicates}')

if __name__ == "__main__":
    main()
