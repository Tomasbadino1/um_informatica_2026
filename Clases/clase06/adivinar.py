numero = 69
intentos = 0

while True:
    n = int(input("Adivina el numero: "))
    intentos += 1
    if numero == n:
        print(f"¡Correcto! Acertaste en {intentos} intentos")
        break
    elif n < numero:
        print("Muy bajo")
    else:
        print("Muy alto")


    
    
# Pedir números hasta que escriban 0
# total = 0

# while True:
#     n = int(input("Número (0 para terminar): "))
#     if n == 0:
#         break
#     total += n

# print(f"Total: {total}")