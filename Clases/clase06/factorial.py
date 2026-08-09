factorial = 1
num = int(input("Ingrese un numero: "))

for i in range(1,num + 1):
    factorial *= i

print(f"N = {num} → factorial = {factorial} ")

