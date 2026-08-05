#Análisis de calificaciones
#Pedir al usuario cuantas notas va a cargar.
#se pone un while para validar que la cantidad de notas es mas que 0, sino se pide que se ingrese de nuevo.
cantidad_notas = int(input("Cantidad de notas: "))
while cantidad_notas <= 0:
    print("Ingrese una cantidad de notas valida")
    cantidad_notas = int(input("Cantidad de notas: "))

#creando la variable notas con una lista vacia, para luego agregar las notas que se ingresaran aqui.
notas = []

#creando un bucle for que para la cantidad de notas se pida un valor. Tambien un while que valide que la nota esta entre 1 y 10, si el valor
#es otro, da un error y se pide que se ingrese de nuevo. A los valores de notas se agregan a la lista de notas.
for n in range(cantidad_notas):
    nota = float(input(f"Nota {n+1}: "))
    while 1 > nota or nota > 10:
        print("Error. Ingrese una nota valida, entre el 1 y el 10")
        nota = float(input(f"Nota {n+1}: "))
    notas.append(nota)

#Creando funciones para el analisis
def promedio(notas):
    return sum(notas) / len(notas)
     
def mas_alta(notas):
    mayor = notas[0]
    for nota in notas:
        if nota > mayor: mayor = nota
    return mayor

def mas_baja(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor: menor = nota
    return menor
        
def contar_aprobados(notas):
    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
    return aprobados
        
def distribucion(notas):
    reprobados_graves = 0
    reprobados = 0
    regulares = 0 
    excelentes = 0
    for nota in notas:
        if nota >= 1 and nota <=3:  reprobados_graves += 1
        elif nota == 4 or nota == 5: reprobados += 1
        elif nota == 6 or nota == 7: regulares += 1
        elif nota >= 8: excelentes += 1
    return f"{reprobados_graves} reprobados graves, {reprobados} reprobados, {regulares} regulares y {excelentes} excelentes"

#ANALISIS
print("=== ANALISIS ===")
print(f"Notas: {notas}")
print(f"Promedio: {promedio(notas):.2f}")
print(f"Más alta: {mas_alta(notas)}")
print(f"Más baja: {mas_baja(notas)}")
print(f"Aprobados: {contar_aprobados(notas)} de {cantidad_notas}")
print(f"Distribución: {distribucion(notas)}")
