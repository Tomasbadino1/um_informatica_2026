#Juego: Ahorcado simplificado
#Importando el módulo random
import random
#Creando la lista de palabras con la funcion random.choice para que elija al azar
lista_palabras = ["parentesis", "software", "ingenieria", "trabajo", "usuario", "tabulador", "videojuego", "computadora", "ahorcado", "espatula"]
palabra_secreta = random.choice(lista_palabras)

#Se crearon 3 variables, guiones, que multiplica la cantidad de caracteres de la palabra secreta por "_".
#Se inicializa la variable fallidas que empieza en 6 y letras usadas en una lista vacia.
guiones = ["_"] * len(palabra_secreta)
fallidas = 6
letras_usadas = []

#while que manejará lo que pasará en el ahorcado:
while fallidas > 0 and "_" in guiones:
    print(" ".join(guiones))
    intentos = input("Ingrese una letra: ").lower()
    
#while de error que indica que debe ingresar la letra de nuevo y un if que indica que ya se probó esta letra y se debe ingresar otra.
    while intentos not in "abcdefghijklmnñopqrstuvwxyz" or len(intentos) != 1:
        print("Error. Ingrese una letra")
        intentos = input("Ingrese una letra: ").lower()
    if intentos in letras_usadas:
        print(f"Ya probaste la letra {intentos}. Prueba otra!")
        continue
#La letra ingresada validada por el while y el if se agrega a la lista letras_usadas.
    letras_usadas.append(intentos)    
#if para reemplazar el guión por la letra.
    if intentos in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == intentos:
                guiones[i] = intentos
#if para restar una vida si la letra es errónea
    if intentos not in palabra_secreta:
        fallidas -= 1
        
    print(f"Letras usadas: {letras_usadas}")
    print(f"Te quedan {fallidas} intentos")

#Informar que pasó (si ganó o perdió)
if "_" not in guiones:
    print(f"\n¡Ganaste! La palabra era {palabra_secreta}")
else:
    print(f"\nPerdiste. Te quedaste sin intentos. La palabra era {palabra_secreta}")