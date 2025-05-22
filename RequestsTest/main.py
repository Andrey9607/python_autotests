import requests


URL="https://api.pokemonbattle.ru/v2"
TOKEN="7396cd81696d08ffbb0e8f203e02c21e"
HEADER={"Content-Type":"application/json","trainer_token":TOKEN}
body_registration={
    "trainer_token":TOKEN,
    "email":"andrei050796@yandex.ru",
    "password":"Sokolov1996"
}

body_confirmation={"trainer_token":TOKEN}

body_create={
    "name":"Бульбазавр",
    "photo_id": -1
}
body_create1 = {
    "pokemon_id": "322960",
    "name": "Sokol",
    "photo_id": -1
}



'''response=requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json=body_registration)

print(response.text)'''

'''response_confirmation=requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json=body_confirmation)
print(response_confirmation.text)'''

'''response_create=requests.post(url=f"{URL}/pokemons",headers=HEADER,json=body_create)
print(response_create.text)'''

'''response_create=requests.put(url=f"{URL}/pokemons",headers=HEADER,json=body_create1)
print(response_create.text)
'''
response_create=requests.post(url=f"{URL}/trainers/add_pokeball",headers=HEADER,json=body_create1)
print(response_create.text)
