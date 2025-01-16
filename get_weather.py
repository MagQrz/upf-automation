import requests # Installera med pip install requests

def get_weather():
    # Förbered en URL för att hämta väderdata
    url = "https://api.open-meteo.com/v1/forecast"
    url += "?latitude=13.7111&longitude=100.5996&current=temperature_2m"

    #13.711188703706584, 100.5996243166667

    print(url)
    # Skicka en förfrågan och hämta data
    response = requests.get(url)
    data = response.json()
    # Returnera temperaturen
    return data["current"]["temperature_2m"]

print(get_weather())