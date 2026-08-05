#Área del círculo
#Pidiendo al usuario el radio de un circulo
radio = float(input("Radio del circulo: "))

# Calculando el área y el perímetro de un círculo
pi = 3.14159
area = pi * radio ** 2
perimetro = 2 * pi * radio

#Mostrando area y perimetro mediante f'strings y con un especificador de decimales despues de la coma.
print(f"Para un circulo de radio {radio}:")
print(f"Area:      {area:.2f} unidades²")
print(f"Perimetro: {perimetro:.2f} unidades")