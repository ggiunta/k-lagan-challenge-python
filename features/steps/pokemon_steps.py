from behave import *
from model.pokemon_model import Pokemon
from helpers.api_helper import APIHelper
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.pokedex_page import *
import time


@given('I do the backend test')
def step_impl(context):
    api_helper = APIHelper()
    normal_pokemons_list_obj = []
    pokemon_limit_to_test = '30'
    pokemon_type_to_test = 'normal'

    pokemons_item = api_helper.get_pokemons(pokemon_limit_to_test).results

    for pokemon in pokemons_item:
        pokemon_details_data = api_helper.get_pokemon_details(pokemon.name)
        pokemon_obj = Pokemon()
        is_normal = False

        for pokemon_type in pokemon_details_data.types:
            pokemon_obj.name = pokemon.name
            pokemon_obj.types.append(pokemon_type.type.name)
            pokemon_type_data = api_helper.get_type_details(pokemon_type.type.name)
            pokemon_type_damage_relations = pokemon_type_data.damage_relations
            pokemon_type_double_damage_from = pokemon_type_damage_relations.double_damage_from

            for weakness in pokemon_type_double_damage_from:
                pokemon_obj.weaknesses.append(weakness.name)


            if pokemon_type.type.name == pokemon_type_to_test:
                is_normal = True

        if is_normal:
            normal_pokemons_list_obj.append(pokemon_obj)

        del pokemon_obj

    context.be_normal_pokemons = normal_pokemons_list_obj

@given('I do the frontend test')
def step_impl(context):
    print('BE Pokemons:')
    for be_normal_pokemon in context.be_normal_pokemons:
        print(be_normal_pokemon.name)
        print(be_normal_pokemon.weaknesses)

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    
    pokedex_page = PokedexPage(driver)
    pokedex_details_page = PokedexDetailsPage(driver)

    print('FE Pokemons:')
    for be_normal_pokemon in context.be_normal_pokemons:
        pokedex_page.navigate_to()
        time.sleep(3)
        pokedex_page.search_for(be_normal_pokemon.name)
        time.sleep(3)
        pokedex_page.select_result(be_normal_pokemon.name.capitalize())
        time.sleep(3)
        print(pokedex_details_page.get_name())
        print(pokedex_details_page.get_weaknesses())
    
    driver.close()
