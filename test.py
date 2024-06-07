import requests

def download_paper(download_url, output_filename):
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(output_filename, 'wb') as file:
            file.write(response.content)
        print(f'Download completed successfully! Saved as {output_filename}')
    else:
        print('Failed to download the paper.')

# Example usage
papers_to_download = [
    {"Title": "Paper 1", "Download_URL": "URL_TO_PAPER_1"},
    {"Title": "Paper 2", "Download_URL": "URL_TO_PAPER_2"},
    # Add more papers as needed
]

for paper in papers_to_download:
    title = paper["Title"]
    download_url = paper["Download_URL"]
    output_filename = f'{title}.pdf'
    download_paper(download_url, output_filename)
