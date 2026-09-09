import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
respuesta = requests.get(url)       # hago el pedido (GET)
 
print(respuesta.status_code)        # 200 = salió bien

# datos = respuesta.json()      # convierte el JSON en un diccionario

# print(datos["name"])          # pikachu
# print(datos["id"])            # 25
# print(datos["weight"])        # 60
# print(datos["types"][0]["type"]["name"])   # electric


import requests
 
def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()             # todo salió bien
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None                 # avisamos y devolvemos None
    
    
url = "https://pokeapi.co/api/v2/pokemon/dragonite"
datos = consultar_api(url)
 
if datos is not None:              # ojo: puede venir None si falló
    print(datos["name"], "pesa", datos["weight"])

nombres = ["pikachu", "charizard", "bulbasaur", "gengar", "snorlax"]
pokemones = []
for nombre in nombres:
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    datos = consultar_api(url)
    if datos is not None:
        pokemones.append(datos)
