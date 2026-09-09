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
    
nombres = ["pikachu", "venusaur", "bulbasaur", "charmander", "snorlax"]
pokemones = []
for nombre in nombres:
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    datos = consultar_api(url)
    if datos is not None:
        pokemones.append(datos)
resumen = []

for p in pokemones:
    resumen.append({
        "nombre": p["name"],
        "tipo": p["types"][0]["type"]["name"],   
        "peso": p["weight"],
    })

#Peso promedio
total = 0
for p in resumen:
    total += p["peso"]
 
#Promedio en hg, y luego a kg
promedio = total / len(resumen)
# print("Peso promedio:", promedio / 10, "kg")   

print(f"{'Nombre':<13}{'Tipo':<13}{'Peso':>10}")
print("-" * 32)

for p in resumen:
    peso_kg = p['peso'] / 10
    print(f"{p['nombre'].capitalize():<13}{p['tipo'].capitalize():<13}{peso_kg:>13.1f}")
    print("-" * 32)
    
#Peso promedio
print("Peso promedio:", promedio / 10, "kg")  

tipo_filtro = "fire"
print(f"Tipo de pokemon elegido: {tipo_filtro}")
for p in resumen:
    if p["tipo"] == tipo_filtro:
        print(f"{p['nombre'].capitalize()} - {p['tipo'].capitalize()}")