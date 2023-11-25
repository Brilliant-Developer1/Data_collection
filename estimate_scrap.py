from bs4 import BeautifulSoup

# Replace 'your_html_code' with the HTML code you provided
your_html_code = """

"""

# Parse the HTML code
soup = BeautifulSoup(your_html_code, 'html.parser')

# Find the <p> tags with the class "paragraph-module_paragraph14Regular__Zfr98" inside the <span> element
estimate_tags = soup.select(
    'span p.paragraph-module_paragraph14Regular__Zfr98')

# Extract and print the "Estimate" values
for i, estimate_tag in enumerate(estimate_tags):
    estimate = estimate_tag.text
    if i % 2 != 0:
        print(estimate)
