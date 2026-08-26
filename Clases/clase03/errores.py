#Errores más comunes a la hora de escribir el codigo:
#SyntaxError: Errores de gramatica, faltan símbolos clave como comillas, paréntesis o dos puntos (:).

#IndentationError: Los espacios o tabulaciones del código están mal alineados.

#NameError: Usas una variable o función que todavía no definiste.

#TypeError: Mezclas tipos de datos incompatibles, como sumar un número con un texto. Los strings son
#inmutables

#ValueError: Una función recibe un dato del tipo correcto pero con un valor absurdo o imposible 
#de procesar (ej. convertir letras a entero).

#ZeroDivisionError: Intentas dividir un número entre cero.

#IndexError: Buscas un número de posición (índice) que no existe en una lista.

#KeyError: Intentas buscar una llave que no existe dentro de un diccionario.

#AttributeError: Pides un atributo o función que el objeto no posee.

#FileNotFoundError: Intentas abrir un archivo que no se encuentra en esa ruta.

# x = []
# y = 5
# # print(x * y + y)
# print(bool(x))

# texto = "10.5"
# int(texto)
# print(texto)

texto = "Desarrollo"
print(texto[1:8:2] + texto[-2])

c = 0
for i in range(4):
    if i % 2 == 0:
        continue
    c += i
print(c)