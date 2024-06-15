import pandas as pd
import subprocess
import os

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

    # Check if the command was successful
    after_files = set(os.listdir('.'))
    foundp=[]
    # Determine the new file
    new_files = after_files - before_files

    if result.returncode == 0 and new_files:
        print("Download succeeded")
        original_filename = new_files.pop()  # Assuming one new file was added
        foundp.append('title')
        # Construct the new filename
        new_filename = f"{año}_{title.replace(' ', '_')}.pdf"
        
        # Rename the file
        os.rename(original_filename, new_filename)
        print(f"File renamed to {new_filename}")
    else:
        print("Download failed or no new file found")
        if result.returncode != 0:
            print(result.stderr)
    return foundp
# Load DataFrame
df = pd.read_csv('filtered_papers.csv',delimiter=';')  # Replace 'papers.csv' with your file path

titles=pd.Series(df['Title'])
año=pd.Series(df['Year'])
for i in range(0,len(titles)):
    print(i)
    lista_papers_found=download_paper_by_title(año[i],titles[i])
print(lista_papers_found)    
    