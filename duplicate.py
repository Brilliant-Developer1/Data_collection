urls = [
    "https://www.ponteonline.com/en/lot-details/auction/631/lot/1416/GATTLE+Lotto+composto+da+gemelli+di+cm+circa+orecchini+di+cm+circa+in",
    "https://www.ponteonline.com/en/lot-details/auction/631/lot/1417/Lotto+composto+da+una+spilla+pendente+in+oro+argento+traforata+di+cm+circa",
    "https://www.ponteonline.com/en/lot-details/auction/631/lot/1418/Demi+parure+in+oro+333+1000+paste+vitree+composta+da+collier+de+chien+moduli",
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
