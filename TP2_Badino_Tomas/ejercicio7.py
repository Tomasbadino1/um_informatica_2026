#Mini-sistema de gestión de biblioteca
#Se inicializa la biblioteca como una lista de listas con 5 libros de ejemplo. Cada sublista guarda [titulo, autor, año, estado], donde el 
#índice 3 (False) significa no prestado, osea, disponible.
biblioteca = [
    ["El Aleph", "Borges", 1949, False], 
    ["Don Quijote de la Mancha", "Miguel de Cervantes", 1605, False], 
    ["Martín Fierro", "José Hernández", 1872, False], 
    ["El principito", "Antoine de Saint-Exupéry", 1943, False], 
    ["Crónica de una muerte anunciada", "Gabriel García Márquez", 1981, False]
]

# Función que imprime un string para dar las opciones disponibles del sistema.
def mostrar_menu():
    print("""
    ===BIBLIOTECA===
    1. Agregar libro
    2. Listar todos los libros
    3. Buscar libro por título
    4. Prestar libro 
    5. Devolver libro
    6. Listar solo disponibles
    7. Listar solo prestados
    8. Estadísticas (cuántos hay, cuántos prestados)
    9. Salir""")

#En la función agregar_libro se creó una variable con una sublista con los datos recibidos y la agrega a la colección principal usando .append().
def agregar_libro(biblioteca, titulo, autor, año):
    libro_nuevo = [titulo, autor, año, False]
    biblioteca.append(libro_nuevo)
    print(f"Libro {titulo}  agregado con éxito")
    
# Se recorre la biblioteca con un bucle for. Se pone "Prestado" o "Disponible" según el valor booleano que se encuentra
#en el índice 3 de cada libro.
def listar_libros(biblioteca):
    print("\n--Listado de libros--")
    for libro in biblioteca:
        estado = "Prestado" if libro[3] == True else "Disponible"
        print(f"{libro[0]} = {estado}")

#Se usa .lower() para pasar toda busqueda a minusculas. Se creó una variable resultados con una lista vacia.
#Se usa un bucle for in para confirmar si la busqueda se encuentra en el primer parámetro de libro (título) que a la vez tambien se 
#cambia a minusculas. El resultado se agrega en la lista de resultados.
def buscar_libro(biblioteca, texto):
    busqueda = texto.lower()
    resultados = []
    for libro in biblioteca:
        if busqueda in libro[0].lower():
            resultados.append(libro)
    return resultados

#Se busca el libro por título comparándolo en minúsculas. Si se encuentra y su índice 3 es False, se cambia a True 
#y se devuelve True para confirmar el préstamo.
def prestar(biblioteca, titulo):
    nombre_libro = titulo.lower()
    for libro in biblioteca:
        if nombre_libro == libro[0].lower():
            if libro[3] == False:
                libro[3] = True
                return True
            elif libro[3] == True:  
                return False
    return False
        
#En la funcion devolver, la lógica es similar a prestar, pero verifica que el libro esté como prestado (True) para volver a ponerlo 
# en False y confirmar la devolución.

def devolver(biblioteca, titulo):
    nombre_libro = titulo.lower()
    for libro in biblioteca:
        if nombre_libro == libro[0].lower():
            if libro[3] == True:
                libro[3] = False
                return True
    return False

#Se usa la función len() para obtener el total de libros y un contador que suma 1 cada vez que un libro tiene 
#el valor True en su índice de estado.
def estadisticas(biblioteca):
    total_libros = len(biblioteca)
    prestados = 0
    for libro in biblioteca:
        if libro[3] == True:
            prestados +=1
    print(f"Cantidad de libros: {total_libros}")
    print(f"Prestados: {prestados}")

#Bucle principal while True que mantiene el menú activo. Se usa int(input()) para la opción y un bloque 
#if-elif para validar la entrada y llamar a la función que corresponda. 
while True:
    mostrar_menu()
    opcion = int(input("Elegir opción: "))
    if opcion == 9:
        break
    
    elif opcion < 1 or opcion > 9:
        print("Error. Por favor, ingresa una opción válida")
        continue
    
    elif opcion == 1:
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        año = int(input("Año: "))
        while año < 0 or año > 2026:
            print("Error. Ingrese un año válido")
            año = int(input("Año: "))
        agregar_libro(biblioteca, titulo, autor, año)
        
    elif opcion == 2:
        listar_libros(biblioteca)
        
    elif opcion == 3:
        texto = input("¿Qué quieres buscar? ")
        libros_encontrados = buscar_libro(biblioteca, texto)
        if len(libros_encontrados) == 0:
            print("Ningún libro encontrado")
        elif len(libros_encontrados) > 0:
            for libro in libros_encontrados:
                print(f"{libro[0]} de {libro[1]} ({libro[2]})")
        
    elif opcion == 4:
        titulo = input("Nombre del libro: ")
        if prestar(biblioteca, titulo):
            print("¡Libro prestado con éxito!")
        else:
            print("No se puede prestar. El libro no existe o ya está prestado")

    elif opcion == 5:
        titulo = input("Nombre del libro: ")
        devolver(biblioteca, titulo)

#Opciones 6 y 7 filtran la lista directamente con un if según el índice 3 del libro.
    elif opcion == 6:
        for libro in biblioteca:
            if libro[3] == False:
                print(f"{libro[0]} - {libro[1]}")
                
    elif opcion == 7:
        for libro in biblioteca:
            if libro[3] == True:
                print(f"{libro[0]} - {libro[1]}")
                
    elif opcion == 8:
        estadisticas(biblioteca)