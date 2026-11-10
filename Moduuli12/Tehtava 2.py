import requests
import json

paikkakunta = input("Anna paikkakunta: ")

api = "4c0564e8188c61001893bd01f87d0bc8"

url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&APPID={api}"

try:
    vastaus = requests.get(url)
    if vastaus.status_code ==200:
        json_vastaus = vastaus.json()
        sää = (json.dumps(json_vastaus["weather"][0]["description"], indent=2))
        asteet = float(json.dumps(json_vastaus["main"]["temp"], indent=2))
        celsius = asteet - 273.15
        print(f"Läpmpötila on {celsius} astetta \n sää: {sää}")
    else:
        print("hakua ei voitu suorittaa")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa")
    