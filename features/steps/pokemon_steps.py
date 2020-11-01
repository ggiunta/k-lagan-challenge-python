from behave import *
from model.pokemon_model import Pokemon
from helpers.api_helper import APIHelper
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@given('I do the backend test')
def step_impl(context):
    api_helper = APIHelper()
    normal_pokemons_list_obj = []

    pokemons_item = api_helper.get_pokemons('1').results

    for pokemon in pokemons_item:
        print(pokemon.url)
        pokemon_details_data = api_helper.get_pokemon_details(pokemon.name)
        pokemon_obj = Pokemon()
        is_normal = False

        for pokemon_type in pokemon_details_data.types:
            print('TYPE: ' + str(pokemon_type.type))
            pokemon_obj.name = pokemon.name
            pokemon_obj.types.append(pokemon_type.type.name)
            pokemon_type_data = api_helper.get_type_details(pokemon_type.type.name)
            pokemon_type_damage_relations = pokemon_type_data.damage_relations
            pokemon_type_double_damage_from = pokemon_type_damage_relations.double_damage_from

            for weakness in pokemon_type_double_damage_from:
                print('WEAKNESS:' + str(weakness))
                pokemon_obj.weaknesses.append(weakness.name)


            if pokemon_type.type.name == 'normal':
                is_normal = True

        if is_normal:
            normal_pokemons_list_obj.append(pokemon_obj)

        del pokemon_obj

    context.be_normal_pokemons = normal_pokemons_list_obj

@given('I do the frontend test')
def step_impl(context):
    print(context.be_normal_pokemons)
    # print(str(context.be_normal_pokemons[0].name))
    # print(str(context.be_normal_pokemons[1].types))
    # print(str(context.be_normal_pokemons[2].weaknesses))
    # print(str(context.be_normal_pokemons[3].types))
    # print(str(context.be_normal_pokemons[4].name))
    # print(str(context.be_normal_pokemons[5].types))
    # print(str(context.be_normal_pokemons[6].weaknesses))

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    driver.get("https://www.pokemon.com/es/pokedex")
    driver.close()
