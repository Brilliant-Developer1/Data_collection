from bs4 import BeautifulSoup

# Sample HTML
html_content = '''

'''

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <li> elements
li_elements = soup.find_all('li')

# Initialize lists to store track codes and titles
track_codes = []
track_titles = []

# Iterate over each <li> element and extract the track code and title
for li in li_elements:
    # Find the second 'col-xs-1 visible-md visible-lg' div which contains the track code
    code_divs = li.find_all('div', class_='col-xs-1 visible-md visible-lg')
    if len(code_divs) > 1:
        track_code = code_divs[1].find('span').get_text(strip=True)
        track_codes.append(track_code)

    # Find the 'col-xs-2 text-left' div which contains the track title
    title_div = li.find('div', class_='col-xs-2 text-left')
    if title_div:
        track_title = title_div.find(
            'small', id='track_title_168').get_text(strip=True)
        track_titles.append(track_title)


# Print all track codes

for code in track_codes:
    print(code)

# Print all track titles

for title in track_titles:
    print(title)
