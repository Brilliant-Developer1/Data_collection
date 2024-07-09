import re
from bs4 import BeautifulSoup

# Your HTML code as a string
html = '''

'''

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <tr> elements with the specified class
tr_elements = soup.find_all('tr', class_='Polaris-IndexTable__TableRow_1a85o')

# Open the file in write mode
with open("newFile.txt", "w", encoding="utf-8") as file:
    # Iterate through each <tr> element and extract id and text content
    for tr in tr_elements:
        # Extract 'id' attribute from <tr> element
        tr_id = tr.get('id', '')

        # Use regex to extract only the numeric part from the id
        numeric_id = re.search(r'\d+', tr_id).group() if tr_id else ''

        # Extract text content from <tr> element with the specified class
        text_content = tr.find(
            'span', class_='Polaris-Text--root_yj4ah Polaris-Text--bodyMd_jaf4s').text.strip()

        # Write the numeric id and text content to the file
        file.write(f"{numeric_id},{text_content}\n")
