from bs4 import BeautifulSoup

html_content = """

"""

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs containing zip codes
zip_code_divs = soup.find_all('div', class_='bVj5Zb FozYP')

# Extract zip codes
zip_codes = [div.text.strip() for div in zip_code_divs]

# Print zip codes in a column view
for zip_code in zip_codes:
    print(zip_code)
