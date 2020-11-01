import requests
import json
from types import SimpleNamespace

class APIHelper(object):
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2'

    def json2obj(self, data):
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    def get_pokemons(self, limit):
        pokemons_resp = requests.get(self.base_url + '/pokemon?limit=' + limit)
        pokemons_data = pokemons_resp.json()

        return self.json2obj(json.dumps(pokemons_data))

    def get_pokemon_details(self, name):
        pokemon_details_resp = requests.get(self.base_url + '/pokemon/' + name)
        pokemon_details_data = pokemon_details_resp.json()

        return self.json2obj(json.dumps(pokemon_details_data))

    def get_type_details(self, poke_type):
        pokemon_type_resp = requests.get(self.base_url + '/type/' + poke_type)
        pokemon_type_data = pokemon_type_resp.json()

        return self.json2obj(json.dumps(pokemon_type_data))