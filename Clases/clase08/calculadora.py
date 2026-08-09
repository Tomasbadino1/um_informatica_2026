def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0: return "error de mensaje"
    return a / b

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
operacion = input("Ingrese una operacion (+,-,*,/): ")

if operacion == "+": print(sumar(a,b))
    
elif operacion == "-": print(restar(a,b))

elif operacion == "*": print(multiplicar(a,b))

elif operacion == "/": print(dividir(a,b))


