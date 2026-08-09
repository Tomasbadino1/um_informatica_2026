frase = "Esta semana hay un examen tonto y un trabajo aburrido"
lista_negra = ["tonto", "aburrido"]

cadena = frase
for palabra in lista_negra:
    asteriscos = "*" * len(palabra)
    cadena = cadena.replace(palabra, asteriscos)
    
    
print(f"original: {frase}")
print(f"nuevo: {cadena}")