import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import os


#faz uma chamada de API e armazena a resposta
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print ("Status code: ",r.status_code)

#armazena a resposta da API em uma variavel
response_dict = r.json()
print("Total repositories:", response_dict['total_count'] )

#explora informacoes sobre os repositorios
repo_dicts = response_dict['items']
names, plot_dicts = [],[]

for repo_dict in repo_dicts:
    
    names. append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'],'label':repo_dict['description'],
    'xlink': repo_dict['html_url'],}
    plot_dicts.append(plot_dict)


#cria a visualização 
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')

command = 'brave python_repos.svg'
os.system(command)

