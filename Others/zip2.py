from bs4 import BeautifulSoup

html_content = """

"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class "vaultTitle" which contains the song title
title_elements = soup.find_all(class_='vaultTitle')

# Extract titles from the elements without the extension and trailing numbers
titles = [element.div.text.split('\n')[1].strip()
          for element in title_elements]

# Print each title on a new line
for title in titles:
    print(title)
