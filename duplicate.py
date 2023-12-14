urls = [
    "",
    # Add the rest of the URLs here
]

# Create an empty list to store duplicate URLs
duplicates = []

# Iterate through the list of URLs
for url in urls:
    # If the URL is already in the duplicates list, it's a duplicate
    if url in duplicates:
        print("Duplicate found:", url)
    else:
        # Otherwise, add it to the duplicates list
        duplicates.append(url)

# If there are no duplicates, print a message
if not duplicates:
    print("No duplicates found.")
