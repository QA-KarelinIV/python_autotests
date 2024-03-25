import requests
import pytest

URL = "https://api.pokemonbattle.me/v2"

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_check_response():
    response = requests.get(url=f'{URL}/trainers')
    trainers = response.json()['data']
    trainer_id = any(trainer['id'] == '2125' for trainer in trainers)
    assert trainer_id