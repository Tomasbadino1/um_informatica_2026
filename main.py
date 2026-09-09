# from datos import pokemones     # traigo la lista
 
# print(len(pokemones))           # 6
# print(pokemones[0]["nombre"])   # pikachu

from fastapi import FastAPI, HTTPException
from datos import pokemones 

app = FastAPI()

# @app.get("/pokemones")
# def listar():
#     return pokemones


@app.get("/pokemones")
def listar(tipo: str = None):    
    if tipo is None:
        return pokemones         
    return [p for p in pokemones if p["tipo"] == tipo]


@app.get("/")              
def inicio():
    return {"mensaje": "¡Mi primera API!"}

# @app.get("/pokemones/{id}")
# def obtener(id: int):
#     for p in pokemones:
#         if p["id"] == id:
#             return p
#     raise HTTPException(status_code=404,
#                         detail="Pokémon no encontrado")


@app.get("/pokemones/{nombre}")
def obtener(nombre: str):
    for p in pokemones:
        if p["nombre"] == nombre.lower():
            return p
    raise HTTPException(status_code=404,
                        detail="Pokémon no encontrado")


@app.get("/pokemones")
def listar(tipo: str = None):     # opcional (por defecto None)
    if tipo is None:
        return pokemones          # sin filtro: todos
    return [p for p in pokemones if p["tipo"] == tipo]

@app.get("/stats")
def estadisticas():
    total = len(pokemones)
    peso_prom = sum(p["peso"] for p in pokemones) / total
    return {"cantidad": total,
            "peso_promedio_kg": round(peso_prom / 10, 2)}


from fastapi import Header, HTTPException
import os
x_api_key = "abcdfg"
 
@app.get("/privado")
def privado(x_api_key: str = Header(None)):
    if x_api_key != os.environ.get("API_KEY"):
        raise HTTPException(status_code=401, detail="No autorizado")
    return {"secreto": "datos protegidos"}
