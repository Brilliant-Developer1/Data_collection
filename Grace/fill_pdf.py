import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Load the CSV data
data = pd.read_csv('Data.csv')

# Print the headers to check column names (use this to debug and find the correct column names)
print(data.columns)

# Load the PDF
template_pdf = '100 waivers-2021.pdf'
output_pdf = 'filled_waivers.pdf'

# Function to create a single page with the new data


def create_overlay(row):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(100, 700, f"Birthdate: {row['Birthdate']}")
    can.drawString(100, 680, f"Home Zip Code: {row['Home Zip Code']}")
    can.drawString(100, 660, f"Date: {row['Date']}")
    can.drawString(100, 640, f"Time1: {row['Time1']}")
    can.drawString(100, 620, f"Package: {row['Package']}")
    can.drawString(100, 600, f"Test: {row['Test']}")
    can.save()
    packet.seek(0)
    return PdfReader(packet)

# Function to fill all PDF forms with the data


def fill_pdf_forms(data, template_pdf, output_pdf):
    reader = PdfReader(open(template_pdf, 'rb'))
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        if i < len(data):  # Ensure we have data for the current page
            overlay = create_overlay(data.iloc[i])
            page.merge_page(overlay.pages[0])
            writer.add_page(page)
        else:
            # Add the page without modification if no data is available
            writer.add_page(page)

    # Save the output
    with open(output_pdf, 'wb') as f:
        writer.write(f)


# Call the function
fill_pdf_forms(data, template_pdf, output_pdf)
