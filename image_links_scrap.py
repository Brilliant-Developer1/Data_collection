from bs4 import BeautifulSoup

# Replace 'your_html_code' with the HTML code you have
your_html_code = """

"""

# Parse the HTML code
soup = BeautifulSoup(your_html_code, 'html.parser')

# Find all anchor (a) tags with href attributes
links = soup.find_all('a', href=True)

# Extract and print the href links
for link in links:
    href = link['href']
    print(href)
