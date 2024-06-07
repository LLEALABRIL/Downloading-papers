import pandas as pd
import subprocess
import PyPDF2
import os
from pdf2image import convert_from_path

def download_paper_by_title(title):
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
    if result.returncode == 0:
        print("Download completed successfully.")
        
    else:
        print(f"Failed to download paper. Return code: {result.returncode}")

# Load DataFrame
df = pd.read_csv('filtered_papers.csv',delimiter=';')  # Replace 'papers.csv' with your file path

titles=pd.Series(df['Title'])
for i in titles:
    print(i)
    download_paper_by_title(i)