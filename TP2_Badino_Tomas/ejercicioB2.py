#Análisis de notas de la cátedra
#Lista de alumnos
alumnos = [
["Ana López", 8, 7, None],
["Pedro Gómez", 4, 6, 7],
["Lucía Pérez", 9, 9, None],
["Juan Díaz", 3, 5, 4],
]
#Acumuladores:
#Estados (promoción, regular o libre)
cant_p = 0
cant_r = 0
cant_l = 0
#Promedio
suma_promedio = 0
#Alumnos
mejor_alumno = ""
mejor_nota = 0
peor_alumno = ""
peor_nota = 0
contador = 0

#Encabezado del informe de alumnos
print("===INFORME===")
print(f"{'ALUMNO':<23} | {'PROMEDIO':>8} | {'ESTADO':<12}")
print("-" * 50)

#Bucle for in
for alumno in alumnos:
    nombre = alumno[0]
    #Calcular promedio con if-elif
    if alumno[3] == None:
        promedio = (alumno[1] + alumno[2]) / 2
        suma_promedio += promedio
    elif alumno[3] != None:
        promedio = (max(alumno[1], alumno[2]) + alumno[3]) / 2
        suma_promedio += promedio

    #Establecer estados según promedios
    if promedio >= 8:
        cant_p += 1
        estado = "PROMOCIÓN"
    elif promedio >= 6:
        cant_r += 1
        estado = "REGULAR"
    elif promedio < 6:
        cant_l += 1
        estado = "LIBRE"
    
    #Mejor y peor alumno:
    #Al ser la primera vuelta (contador = 0) el alumno va a ser el peor y el mejor a la vez.
    if contador == 0:
        mejor_alumno = nombre
        mejor_nota = promedio
        peor_alumno = nombre
        peor_nota = promedio
    else:
        if mejor_nota < promedio:
            mejor_alumno = nombre
            mejor_nota = promedio
        if peor_nota > promedio:
            peor_alumno = nombre
            peor_nota = promedio
    
    #Nombres en el cuadro de cada alumno, con promedio y estado:
    print(f"{nombre:<20} | {promedio:>8} | {estado:<12}")
    
    #Sumamos 1 para que la proxima no sea la primera vuelta
    contador += 1

#Promedio final: con el acumulador de suma_promedio / len(alumnos) (la cantidad de alumnos)
promedio_final = suma_promedio / len(alumnos)

#Estadísticas finales: cantidad de cada categoría, promedio del curso, mejor y peor alumno
print("-" * 50)
print(f"Cantidad de promocionados: {cant_p}")
print(f"Cantidad de regulares:     {cant_r}")
print(f"Cantidad de libres:        {cant_l}")
print("-" * 50)
print(f"Promedio del curso:        {promedio_final}")
print("-" * 50)
print(f"Mejor alumno:              {mejor_alumno} con {mejor_nota}")
print(f"Peor alumno:               {peor_alumno} con {peor_nota}")
