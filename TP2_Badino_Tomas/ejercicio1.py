#Version mejorada de: Conversor de temperaturas
#Definiendo funciones de temperaturas a otras
def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def celsius_a_kelvin(c):
    return c + 273.15    

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9
    
def fahrenheit_a_kelvin(f):  
    return fahrenheit_a_celsius(f) + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def kelvin_a_fahrenheit(k):
    return kelvin_a_celsius(k) * 9/5 + 32

#Pidiendole al usuario que ingrese una temperatura, luego que ingrese cual sera la unidad de origen y a cual quiere pasarlo.
#Tambien se aplicó la funcion .strip y .upper para que lo que el usuario ingrese se separe en distintos elementos  
#y para que a este elementos si la unidad está en minusculas se conviertan en mayusculas.
#Se uso un while para la unidad_origen y unidad_destino que valide que si alguna de estas dos no es F, C o K muestre un error y se
#vuelve a pedir una unidad.
#Tambien se asigno la variable resultado.

temperatura = float(input("Temperatura: "))

unidad_origen = (input("Unidad de origen(F,C,K): ")).strip().upper()
while unidad_origen not in ["F", "C", "K"]:
    print("Error, ingresa F, C o K")
    unidad_origen = (input("Unidad de origen(F,C,K): ")).strip().upper()

unidad_destino = (input("Unidad de destino(F,C,K): ")).strip().upper()
while unidad_destino not in ["F", "C", "K"]:
    print("Error, ingresa F, C o K")
    unidad_destino = (input("Unidad de destino(F,C,K): ")).strip().upper()
    
resultado = 0


#Utilizando el patron if-elif-else para decidir que funcion llamar segun las unidades elegidas  
if unidad_origen == "C" and unidad_destino == "F":
    resultado = (celsius_a_fahrenheit(temperatura))
        
elif unidad_origen == "C" and unidad_destino == "K":
    resultado = (celsius_a_kelvin(temperatura))
        
elif unidad_origen == "F" and unidad_destino == "C":
    resultado = (fahrenheit_a_celsius(temperatura))
        
elif unidad_origen == "F" and unidad_destino == "K":
    resultado = (fahrenheit_a_kelvin(temperatura))    
        
elif unidad_origen == "K" and unidad_destino == "C":
    resultado = (kelvin_a_celsius(temperatura))

elif unidad_origen == "K" and unidad_destino == "F":
    resultado = (kelvin_a_fahrenheit(temperatura))

elif unidad_origen == unidad_destino:
    resultado = "Las unidades de origen y destino son la misma."

else:
    resultado = "Ingresa una unidad valida."

#Mostrando resultado
#Si el resultado es un numero, haria el print de la conversion
if type(resultado) != str:
    print(f"{temperatura}°{unidad_origen} equivalen a {resultado:.2f}°{unidad_destino}")
    
#Si el resultado es un texto, daría el mensaje de error
else:
    print(resultado)