import requests

URL = "https://api.pokemonbattle.me/v2"
HEADERS = {"Content-Type": "application/json", "trainer_token": "//token скрыт"}
BODY = {
    "name": "bugaga",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=BODY)
print(response.text)

BODY2 = {
    "pokemon_id": "14780",
    "name": "Питоняша",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=BODY2)
print(response.text)

BODY3 = {
    "pokemon_id": "14815"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=BODY3)
print(response.text)