#WHILE:
contador = 0

# while contador < 13:
#     contador += 1
#     print(contador) 
    
# print("el while llego a su fin")


n = int(input("Ingrese un numero: "))
resultado = ""
for i in range(1, n + 1):
    resultado = resultado + str(i) + " "

print(resultado)