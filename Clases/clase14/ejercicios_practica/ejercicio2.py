#Ejercicio 2 · El clima de tu ciudad    
#API: Open-Meteo
import requests

url = "https://api.open-meteo.com/v1/forecast"

def consultar_api(url, params=None):
    try:
        r = requests.get(url, params=params,timeout=5)
        r.raise_for_status()
        return r.json()           
    except requests.exceptions.RequestException as e:
        print("Error al consultar la API:", e)
        return None
    
parametros = {
    "latitude":-33.14587,
    "longitude": -64.31735,
    "current_weather": "true"
}

datos = consultar_api(url, parametros)

if datos is not None:
    clima_actual = datos.get("current_weather")
    
    if clima_actual is not None:
        temperatura = clima_actual.get("temperature")
        vel_viento = clima_actual.get("windspeed")
        
        
        print("CLIMA ACTUAL EN RIO CUARTO")
        print(f"Temperatura: {temperatura}")
        print(f"Velocidad del viento: {vel_viento}")

    else:
        print("No se encontraron datos del clima actual en la respuesta.")
else:
    print("No se pudo obtener información del clima.")