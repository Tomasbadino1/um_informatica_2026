#Área y perímetro de un rectángulo
#Pidiendo al usuario que ingrese la base y altura de un rectángulo
base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

#Definiendo las variables área y perímetro con su fórmula
area = base * altura
perimetro = 2 * (base + altura)

#Mostrando resultados mediante f'strings
print(f"Resultados:")
print(f"Área: {area} m²")
print(f"Perímetro: {perimetro} m")