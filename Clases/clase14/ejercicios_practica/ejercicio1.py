#Ejercicio 1 · Ficha de un Pokémon    
import requests

url = "https://pokeapi.co/api/v2/pokemon/charizard"


def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()           
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None
    
datos = consultar_api(url)

if datos is not None:
    print(f"Nombre: {datos["name"]}")
    print(f"ID: {datos["id"]}")
    print(f"Altura: {datos["height"]}")
    print(f"Peso: {datos["weight"] / 10}")

