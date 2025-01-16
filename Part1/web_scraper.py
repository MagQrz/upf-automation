import requests
from bs4 import BeautifulSoup

#response = requests.get("https://docs.python.org/3/")
response = requests.get("https://google.com/")

# print(response.text)

# Skapa en BeautifulSoup-instans
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('a') # Hitta alla <h1>-element / <a>

for title in titles: # Skriv ut titlarna
    print(title.text)