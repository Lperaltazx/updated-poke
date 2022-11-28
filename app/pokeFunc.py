import requests as req

def getpoke(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    resp = req.get(url)
    if resp.ok:
        dct = resp.json()
        pokemon_dict =  {'name': dct['name'],   
            'ability': dct['abilities'][0]['ability']['name'],
            'base_experience': dct['base_experience'],
            'sprite_front_shiny': dct['sprites']['front_shiny'],
            'base_stat_attack': dct['stats'][1]['base_stat'],
            'base_stat_hp': dct['stats'][0]['base_stat'],
            'base_stat_defense': dct['stats'][2]['base_stat']
            }
        return pokemon_dict
    else:
        return 'Whos that Pokemon? make sure you spell it right?'