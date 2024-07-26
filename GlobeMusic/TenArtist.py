# Open the input file in read mode
with open('/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt', 'r') as infile:
    # Read all lines and strip any leading/trailing whitespace
    artists = [line.strip() for line in infile]

# Open the output file in write mode
with open('/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt', 'w') as outfile:
    # Loop through each artist name
    for artist in artists:
        # Print the artist name 10 times
        for _ in range(40):
            outfile.write(artist + '\n')

print("Output written to output.txt")
