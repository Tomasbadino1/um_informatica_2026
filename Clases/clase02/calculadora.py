def sumar(numeros):
    return sum(numeros)
print(sumar([55,45]))

def restar(numeros):
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado = resultado - numero
    return resultado

print(restar([6,5,5]))


    
Variable = "hola mundo"
print(type(Variable))
edad = 18

print(type(15.5))


#numero = input("Ingrese un numero cualquiera: ")
#resultado_entero = int(numero) * 2
#print(resultado_entero)

#numero = input("Ingrese un numero cualquiera: ")
#resultado_flotante = float(numero) * 2
#print(resultado_flotante)


def saludar(nombre):
    return f"Hola {nombre} como estas mi amigo?"

print(saludar("Maxi"))