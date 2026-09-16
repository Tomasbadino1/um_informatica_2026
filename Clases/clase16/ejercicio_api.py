import csv
import requests

url = "https://pokeapi.co/api/v2/pokemon/"

def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()           
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None      

datos = consultar_api("https://pokeapi.co/api/v2/pokemon/ditto")
resumen = []

for i in range(1,10):
    datos = consultar_api(f"{url}{i}")
    if datos is not None:
        resumen.append({
            "nombre": datos["name"],
            "tipo": datos["types"][0]["type"]["name"],
            "peso": datos["weight"] / 10
            })

print(resumen)

with open("pokemon.csv", "a", newline="") as f:     
    escritor = csv.writer(f)
    for p in resumen:
        escritor.writerow([p["nombre"], p["peso"]])
