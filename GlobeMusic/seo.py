def process_song_titles(main_input_file, seo_input_file, output_file):
    # Read the main song titles from the main input file
    with open(main_input_file, 'r') as file:
        song_titles = file.read().strip().split('\n')

    # Read the SEO titles from the SEO input file
    with open(seo_input_file, 'r') as file:
        seo_titles = file.read().strip().split('\n')

    # Split the main song titles into chunks of 10
    chunk_size = 40
    chunks = [song_titles[i:i + chunk_size]
              for i in range(0, len(song_titles), chunk_size)]

    # Index for the SEO titles to repeat from the beginning if necessary
    seo_index = 0
    seo_len = len(seo_titles)

    # Replace the 5th, 8th, and 10th titles in each chunk with SEO titles
    for chunk in chunks:
        if len(chunk) >= 1: 
            chunk[0] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 4:
            chunk[3] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 8:
            chunk[7] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 10:
            chunk[9] = seo_titles[seo_index % seo_len]
            seo_index += 1        
        if len(chunk) >= 12:
            chunk[11] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 16:
            chunk[15] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 20:
            chunk[19] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 23:
            chunk[22] = seo_titles[seo_index % seo_len]
            seo_index += 1    
        if len(chunk) >= 25:
            chunk[24] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 28:
            chunk[27] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 30:
            chunk[29] = seo_titles[seo_index % seo_len]
            seo_index += 1
        if len(chunk) >= 32:
            chunk[31] = seo_titles[seo_index % seo_len]
            seo_index += 1    
        if len(chunk) >= 35:
            chunk[34] = seo_titles[seo_index % seo_len]
            seo_index += 1              

    # Write the modified chunks to the output file
    with open(output_file, 'w') as file:
        for chunk in chunks:
            for title in chunk:
                file.write(title + '\n')


# Specify the input and output files
main_input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
seo_input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input2.txt'
output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

# Process the song titles and write to the output file
process_song_titles(main_input_file, seo_input_file, output_file)


