import csv
import requests
import sqlite3

url = "https://pokeapi.co/api/v2/pokemon/"

def consultar_api(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()           
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None      
    
resumen = []

for i in range(1,10):
    datos = consultar_api(f"{url}{i}")
    if datos is not None:
        resumen.append({
            "nombre": datos["name"],
            "tipo": datos["types"][0]["type"]["name"],
            "peso": datos["weight"] / 10
            })
    
            
with open("Clases\\clase16\\pokemon.csv", "w", newline="") as f:
    campos = ["nombre", "tipo", "peso"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()      
    for p in resumen:
        escritor.writerow(p)           
    

con = sqlite3.connect("pokedex.db")   # abre (o crea) la base
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS pokemones "
                "(nombre TEXT, peso INTEGER)")
for p in resumen:
    cur.execute("INSERT INTO pokemones VALUES (?, ?)", (p['nombre'], p['peso']))
con.commit()                          # confirma los cambios

for fila in cur.execute("SELECT * FROM pokemones"):
    print(fila)
