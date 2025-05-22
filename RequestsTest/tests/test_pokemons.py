import requests
import pytest

URL="https://api.pokemonbattle.ru/v2"
TOKEN="7396cd81696d08ffbb0e8f203e02c21e"
HEADER={"Content-Type":"application/json","trainer_token":TOKEN}
trainer_id = 33494
trainer_name = "Sokol"




def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': trainer_id})
    assert response.status_code == 200

def test_trainer_name():
    trainer_name = "Sokol"  
    response = requests.get(url=f'{URL}/trainers/33494', params={'trainer_name': trainer_name})
    
   