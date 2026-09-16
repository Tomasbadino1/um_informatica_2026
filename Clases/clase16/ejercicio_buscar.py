import csv
import os
import requests

directorio_script = os.path.dirname(__file__)
ruta_csv = os.path.join(directorio_script, "buscar_pokemon.csv")

url = "https://pokeapi.co/api/v2/pokemon/"

def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()           
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None      

datos = consultar_api("https://pokeapi.co/api/v2/pokemon/")
pokemones = []
busqueda = input("Ingrese el nombre del pokémon: ").lower().strip()


#Intentamos abrir el archivo, y si es que no existe usamos try/except
try:
    with open(ruta_csv, "r") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            pokemones.append(fila["nombre"].lower())
except FileNotFoundError:
    pass


if busqueda in pokemones:
    print(f"El pokémon {busqueda} ya está guardado.")
else:
    datos_poke = consultar_api(f"https://pokeapi.co/api/v2/pokemon/{busqueda}")
    if datos_poke is not None:
        with open(ruta_csv, "a", newline="") as f:   
            campos = ["nombre", "tipo", "peso"]  
            escritor = csv.DictWriter(f, fieldnames=campos)
            
            #si el archivo no tiene datos, se hace el encabezado    
            if len(pokemones) == 0: escritor.writeheader()

            nuevo_pokemon = {
            "nombre": datos_poke["name"],
            "tipo": datos_poke["types"][0]["type"]["name"],
            "peso": datos_poke["weight"] / 10
            }
            escritor.writerow(nuevo_pokemon)
            print(f"Guardado con exito el pokémon {datos_poke['name']} en el archivo CSV.")
            

    else:
        print(f"El pokémon {busqueda} no existe en la PokeAPI")