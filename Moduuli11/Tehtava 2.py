
import requests


API_AVAIN = "OMA_API_AVAIN_TAHAN"


kaupunki = input("Anna paikkakunta: ")


osoite = "https://api.openweathermap.org/data/2.5/weather"

parametrit = {
    "q": kaupunki,
    "appid": API_AVAIN,
    "lang": "fi"
}

vastaus = requests.get(osoite, params=parametrit)
data = vastaus.json()

if vastaus.status_code == 200:
    saa = data["weather"][0]["description"]
    kelvin = data["main"]["temp"]

    celsius = kelvin - 273.15

    print("Säätila:", saa)
    print("Lämpötila:", round(celsius, 1), "°C")

else:
    print("Säätietojen hakeminen epäonnistui.")
