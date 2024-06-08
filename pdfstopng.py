import os
import fitz  # PyMuPDF
from PIL import Image

# Directory containing PDF files
pdf_directory = '.'  # Replace with your directory path
output_directory = './result/'  # Replace with your desired output directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)
def get_page_and_name(pdf_filename):
    if "specific_condition" in pdf_filename:  # Replace with your specific condition
        page_number = 1  # Extract the second page (0-indexed, so 1 is the second page)
        output_name = f"{os.path.splitext(pdf_filename)[0]}_first_page.png"
    else:
        page_number = 0  # Extract the first page (0-indexed)
        output_name = f"{os.path.splitext(pdf_filename)[0]}_first_page.png"
    return page_number, output_name
def get_page_and_name1(pdf_filename):
    page_number = 1  # Extract the second page (0-indexed, so 1 is the second page)
    output_name = f"{os.path.splitext(pdf_filename)[0]}_first_page.png"
    return page_number, output_name
# Process each PDF file in the directory

list=['2006_Fiber models for the failure of composite materials_first_page.pdf']
#for filename in os.listdir(pdf_directory):
'''for filename in os.listdir(list):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        pdf_document = fitz.open(pdf_path)
        
        # Get the page number to extract and the output file name
        page_number, output_name = get_page_and_name(filename)
        
        # Check if the PDF has enough pages
        if pdf_document.page_count > page_number:
            page = pdf_document.load_page(page_number)
            
            # Increase DPI for higher definition
            zoom_x = 2.0  # horizontal zoom
            zoom_y = 2.0  # vertical zoom
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat)
            output_path = os.path.join(output_directory, output_name)
            pix.save(output_path)
            
            print(f"Processed {filename} -> {output_path}")
        else:
            print(f"{filename} does not have a page number {page_number + 1}")

print("All PDF files have been processed.")
#Extrayendo la segunda hoja solo para algunos:
'''
filename='2008_SIMULAcAO_DE_RECUPERAcAO_TERMICA_EM_ESCALA_MICROSC.pdf'
pdf_path = os.path.join(pdf_directory, filename)
pdf_document = fitz.open(pdf_path)

# Get the page number to extract and the output file name
page_number, output_name = get_page_and_name1(filename)

# Check if the PDF has enough pages
if pdf_document.page_count > page_number:
    page = pdf_document.load_page(page_number)
    
    # Increase DPI for higher definition
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_directory, output_name)
    pix.save(output_path)
    
    print(f"Processed {filename} -> {output_path}")
