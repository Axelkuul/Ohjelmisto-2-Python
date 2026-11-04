import requests

pokemon = input("Anna pokemonin nimi: ")

url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

vastaus = requests.get(url)


if vastaus.status_code==200:
    vastaus = vastaus.json()

    print(f"Nimi: {vastaus["name"]}")
    print(f"Tyyppi: {vastaus["types"][0]["type"]["name"]}")
else:
    print("Pokemonia ei löytynyt tai hakua ei voitu suorittaa")