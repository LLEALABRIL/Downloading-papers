import requests
from bs4 import BeautifulSoup
import re
import os

def search_scholar_and_download_pdf(title, save_path):
    # Prepare the search URL
    search_url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

    # Set headers to simulate a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a request to Google Scholar
    response = requests.get(search_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first result
        result = soup.find('div', class_='gs_ri')
        
        if result:
            title = result.find('h3', class_='gs_rt').text
            authors = result.find('div', class_='gs_a').text
            snippet = result.find('div', class_='gs_rs').text

            # Print the paper information
            print(f"Title: {title}")
            print(f"Authors: {authors}")
            print(f"Snippet: {snippet}")

            # Try to find PDF link in the result
            pdf_link = None
            for link in result.find_all('a', href=True):
                if re.search(r'\.pdf$', link['href']):
                    pdf_link = link['href']
                    break
            
            if pdf_link:
                print(f"PDF Link: {pdf_link}")
                download_pdf(pdf_link, save_path, title)
            else:
                print("PDF link not found.")
        else:
            print("No results found.")
    else:
        print("Request to Google Scholar failed.")

def download_pdf(pdf_url, save_path, title):
    # Set headers to simulate a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make a request to download the PDF
    response = requests.get(pdf_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the PDF to the specified path
        pdf_name = re.sub(r'\W+', '_', title) + '.pdf'
        pdf_path = os.path.join(save_path, pdf_name)
        
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        
        print(f"PDF downloaded and saved as: {pdf_path}")
    else:
        print("Failed to download")
import pandas as pd

df = pd.read_csv('doc.csv')

# Print the DataFrame
element = df.iloc[0,0]
#print(element)
#search_scholar(element)
search_scholar_and_download_pdf(element, "paper.pdf")
