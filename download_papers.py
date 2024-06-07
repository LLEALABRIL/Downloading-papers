import pandas as pd   
import requests
from bs4 import BeautifulSoup

def download_paper(url, target_title, output_filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send a request to the page with the list of papers
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('Failed to retrieve the page.')
        return

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all paper titles and their download links
    papers = soup.find_all('a', {'class': 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'})
    
    # Loop through each paper to find the matching title
    found = False
    for paper in papers:
        title = paper.text.strip()
        if target_title.lower() in title.lower():
            found = True
            download_url = paper['href']
            break
    
    if not found:
        print(f'Paper with title "{target_title}" not found.')
        return
    
    # Download the paper
    paper_response = requests.get(download_url, headers=headers)
    if paper_response.status_code == 200:
        with open(output_filename, 'wb') as file:
            file.write(paper_response.content)
        print(f'Download completed successfully! Saved as {output_filename}')
    else:
        print('Failed to download the paper.')

df = pd.read_csv('filtered_papers.csv',sep=";")
dfo = df.sort_values(by='Year')

print(dfo)
element = df.iloc[0,0]
#print(element)]

email = "leidy.leal@uptc.edu.co"
password = "mileleal"
article_title = element

# Example usage
url = 'https://www.researchgate.net/scientific-contributions/Hans-J-Herrmann-2123959106'  # Replace with the actual URL
target_title = 'Modeling public opinion control by a charismatic leader'
output_filename = 'downloaded_paper.pdf'
download_paper(url, target_title, output_filename)

