import pandas as pd
import requests
import subprocess
import os
import scholarly
import re

def get_doi_from_title(title):
    url = 'https://api.crossref.org/works'
    params = {
        'query.title': title,
        'rows': 1  # Limit the results to 1 for simplicity
    }
    
    # Send the GET request to the CrossRef API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'message' in data and 'items' in data['message'] and len(data['message']['items']) > 0:
            # Extract the DOI from the first item in the results
            doi = data['message']['items'][0]['DOI']
            return doi
        else:
            return 'DOI not found'
    else:
        return f'Error: {response.status_code}'

# Example usage
#title = 'Example Paper Title'


def download_paper_by_title(año,title):
    before_files = set(os.listdir('.'))

    # Construct the command as you would run it in the terminal
    
    command = ['scidownl', 'download', '--title', title]
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output from the command
    if result.stdout:
        print("Output:", result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
        print('here')

    # Check if the command was successful
    after_files = set(os.listdir('.'))
    foundp=[]
    # Determine the new file
    new_files = after_files - before_files
    rta=True
    if result.returncode == 0 and new_files:
        print("Download succeeded")
        original_filename = new_files.pop()  # Assuming one new file was added
        #foundp.append('title')
        # Construct the new filename
        new_filename = f"{año}_{title.replace(' ', '_')}.pdf"
        # Rename the file
        os.rename(original_filename, new_filename)
        print(f"File renamed to {new_filename}")
    else:
        print("Download failed or no new file found")
        rta=False
        #get_doi_from_title(title)
        
        #if result.returncode != 0:
        #    print(result.stderr)
    return rta
# Load DataFrame
df = pd.read_excel('Yenny/file.xlsx')  # Replace 'papers.csv' with your file path
titles=pd.Series(df['ARTIGO'])

numbers = range(2, 104)
df['Numbers'] = numbers

numero=pd.Series(df['Numbers'])
for i in range(0,len(titles)):
    print(i)
    if(i==2):
        state=download_paper_by_title(numero[i],titles[i])
        if(state==False):
            if(":" in titles[i]):
                titles[i]=re.sub(r'[:]', '', titles[i])
                print(titles[i])
            download_paper_by_title(numero[i],titles[i])

#print(lista_papers_found)