from bs4 import BeautifulSoup

# Sample HTML code
html_code = '''

'''

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Find all <p> elements with class "text-dark"
# p_elements = soup.find_all('p', class_='text-dark')

# # Iterate through the <p> elements and extract the "sold" data or print 0 if not found
# for p in p_elements:
#     sold_tag = p.find('span', class_='sold')
#     if sold_tag:
#         sold_data = sold_tag.get_text()
#     else:
#         sold_data = "0"
#     print(sold_data)

# Find the <p> tags with the class "label-module_label14Medium__uD9e-" inside the <span> element with class "css-7d31lt"
lot_sold_tags = soup.select(
    'span.css-7d31lt p.label-module_label14Medium__uD9e-')

# Extract and print the "Lot Sold" values or "0" if no value is found
for i, lot_sold_tag in enumerate(lot_sold_tags):
    lot_sold = lot_sold_tag.text
    if i % 2 != 0:
        if lot_sold:
            print(lot_sold)
        else:
            print("0")
