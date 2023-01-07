import json
import pygal
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
import os


#carrega os dados em uma lista 
filename = 'data/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

#constroi um dicionario com dados das populacoes
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] =='2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

#agrupa os paises em tres niveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop <10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_2[cc] = pop

#ve quantos paises estao em cada nivel
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#66ff33', base_style = LCS)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
file = 'world_population.svg'
wm.render_to_file(file)

command = 'brave ' + file
os.system(command)