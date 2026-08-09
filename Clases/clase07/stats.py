n = int(input("Cantidad de notas: "))
notas = []

while True:
    for nota in range(n):
        nota = float(input("nota: "))
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    nota_alta = max(notas)
    nota_baja = min(notas)

    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1

    print(f"""Lista completa: {notas} - Promedio: {promedio:.2f} - Nota mas alta: {nota_alta} - Nota mas baja: {nota_baja} - Cantidad de aprobados: {aprobados}""")
    
    
    s = input("¿Quieres seguir poniendo notas? (s/n): ")
    n = True
    if s == False:
        print("Gracias por las notas")
        break