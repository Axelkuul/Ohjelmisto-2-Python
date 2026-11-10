import requests
import json

url = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(url)
    if vastaus.status_code ==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus["value"], indent=2))
    else:
        print("hakua ei voitu suorittaa")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa")

