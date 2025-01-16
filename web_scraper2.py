import requests
from bs4 import BeautifulSoup

response = requests.get("https://docs.python.org/3/")
#response = requests.get("https://google.com/")

# print(response.text)

# Skapa en BeautifulSoup-instans
soup = BeautifulSoup(response.text, 'html.parser')
footers = soup.find_all("div", class_="footer")

for footer in footers: # Skriv ut titlarna
    footer_part = footer.text.split("Copyright")[1].strip()

    print(footer_part.split("2001-")[1].split(",")[0])