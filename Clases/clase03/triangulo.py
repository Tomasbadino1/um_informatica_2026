print(2 ** 0.5)


edad = 19
print("hola")



#triangulo
#a = float(input("Ingrese el lado a: "))
#b = float(input("Ingrese el lado b: "))
#c = float(input("Ingrese el lado c: "))
#if (a < b + c) and (b < a + c) and (c < a + b):
#    print("Tu triangulo es valido")
#    
#elif a == b and b == c:
#   print("Tu triangulo es isosceles")
    
#elif a == b or b == c or a == c:
#    print("Tu triangulo es equilatero")
    
    
#triangulo
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))
valido = (a < b + c) and (b < a + c) and (c < a + b)
equilatero = a == b or b == c or a == c
isosceles = a == b and b == c
print(f"Tu triangulo es valido: {valido}, equilatero: {equilatero}, isosceles: {isosceles}")