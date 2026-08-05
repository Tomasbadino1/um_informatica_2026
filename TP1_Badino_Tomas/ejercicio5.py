#Distancia entre dos puntos
#Pidiendo al usuario las coordenadas de dos puntos del plano (x1, y1) y (x2, y2)
print("Punto 1")
x1 = int(input("  x1: "))
y1 = int(input("  y1: "))
print("Punto 2")
x2 = int(input("  x2: "))
y2 = int(input("  y2: "))

#Definiendo la formula de distancia entre ellos
distancia = ((x2 - y1) ** 2 + (y2 - y1) ** 2) ** 0.5

#Mostrando resultado de distancia mediante f'string
print(f"Distancia entre ({x1}, {y1}) y ({x2}, {y2} = {distancia})")