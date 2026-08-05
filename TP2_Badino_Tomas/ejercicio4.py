#Procesador de palabras
#Pidiendo al usuario un texto
texto = input("Ingresá un texto: ")

#se crearon funciones. La función de ver la cantidad de palabras del texto se usa len() para contar la cantidad de palabras que ya fueron separadas
#con el .split()
def cantidad_palabras(texto):
    return len(texto.split()) 

#La función de cantidad de vocales empieza inicializandola con la variable de vocales en 0. Se recorre cada caracter del texto con el bucle y se
#agrega un if para que cuente caracter por caracter si se encuentra en el string de vocales.
def cantidad_vocales(texto):
    vocales = 0
    for caracter in texto:
        if caracter in "aeiouáéíóúAEIOUÁÉÍÓÚ":
            vocales +=1
    return vocales

#La funcion de mas_larga y mas_corta tienen una estructura similar. Comienza con una variable palabras que separa palabra por palabra el texto 
#mandado usando .split(). Se inicializa una variable con la primera palabra de la lista para tener un punto de referencia y se recorre el 
#resto de la colección con un bucle for. En cada vuelta, se usó un if len() para comparar el largo actual con el largo de la guardada, 
#actualizando la variable y devolviendo con return.
def mas_larga(texto):
    palabras = texto.split()
    if not palabras: 
        return "Sin palabras"
    larga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(larga): 
            larga = palabra
    return larga

def mas_corta(texto):
    palabras = texto.split()
    if not palabras: 
        return "Sin palabras"
    corta = palabras[0]
    for palabra in palabras:
        if len(palabra) < len(corta): 
            corta = palabra
    return corta

#La función de reemplazar vocales empieza inicializando con la variable vocales y un bucle for que recorre vocal por vocal del texto y se reemplaza
#esa vocal por *.
def replace_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    for vocal in vocales:
        texto = texto.replace(vocal, "*")
    return texto

#La funcion de orden inverso separa con .split() la lista de palabras, luego las invierte con [::-1] y por último se une la versión invertida con
#.join
def orden_inverso(texto):
    lista_de_palabras = texto.split()
    invertida = lista_de_palabras[::-1]
    return " ".join(invertida)

#ESTADÍSTICAS
print(f"Palabras: {cantidad_palabras(texto)}")
print(f"Vocales: {cantidad_vocales(texto)}")
print(f"Más larga: {mas_larga(texto)}")
print(f"Más corta: {mas_corta(texto)}")
print(f"Sin vocales: {replace_vocales(texto)}")
print(f"Orden inverso: {orden_inverso(texto)}")