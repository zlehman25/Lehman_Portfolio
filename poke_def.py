#importing API tools
import requests
import json

#defining a list to feed through the API scraper function
current_team = ['pikachu', 'mew', 'snorlax', 'charizard', 'zapdos', 'seedot']

#defining a class and creating functions
class Poke:
    #this function takes an input (poke) and checks the poke API website to see if the url works. If it does, it loads the contents into a JSON file
    def get_data(poke):
        url = ("https://pokeapi.co/api/v2/pokemon/" + poke)
        response = requests.get(url)
        if response.status_code == 200:
            output = json.loads(response.text)
            return output
        return None

    #this function takes each element in the current_team list and returns the name of the pokemon
    def get_name(poke):
        for i in current_team:
            mon = Poke.get_data(i)
            name = mon['name']
            print(name)

    #this function takes each element in the current_team list and returns the type(s) of the pokemon
    def get_type(poke):
        for i in current_team:
            mon = Poke.get_data(i)
            types = [typ['type']['name'] for typ in mon ['types']]
            print(types)

#running the functions
Poke.get_name(current_team)
Poke.get_type(current_team)