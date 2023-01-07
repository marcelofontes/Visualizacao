from pygal_maps_world import i18n

def get_country_code(country_name):
    #devolve o codigo de duas letras do pygal para um país, dado o seu nome
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
            #se o pais nao foi encontrado, devolve None
    return None



