import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

def login_researchgate(email, password):
    login_url = "https://www.researchgate.net/login"
    session = requests.Session()
    
    # Get the login page to retrieve the authenticity token
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')
    
    # Extract authenticity token
    token_input = soup.find('input', {'name': 'authenticity_token'})
    if not token_input:
        print("Failed to find authenticity token on the login page.")
        return None
    
    token = token_input.get('value')
    
    # Prepare login data
    login_data = {
        'utf8': '✓',
        'authenticity_token': token,
        'login': email,
        'password': password,
        'remember': '1'
    }
    
    # Perform login
    response = session.post(login_url, data=login_data)
    
    # Check if login was successful
    if "dashboard" in response.url or response.url == "https://www.researchgate.net/home":
        print("Login successful!")
        return session
    else:
        print("Login failed!")
        return None
    
df = pd.read_csv('filtered_papers.csv',sep=";")
dfo = df.sort_values(by='Year')

print(dfo)
element = df.iloc[0,0]
#print(element)]

email = "leidy.leal@uptc.edu.co"
password = "mileleal"
article_title = element
session = login_researchgate(email, password)
if session:
    # Now you can use `session` to make authenticated requests
    profile_url = "https://www.researchgate.net/profile/Your_Profile"
    profile_page = session.get(profile_url)
    print(profile_page.text) 