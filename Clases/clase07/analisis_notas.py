notas = [8, 6, 9, 4, 10, 7, 5, 8, 3, 9]
total = 0
aprobados = 0
desaprobados = 0
for nota in notas:
    total += nota
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados +=1
print(f"Suma de las notas = {total}")
print(f"Cantidad de aprobados = {aprobados}")
print(f"Cantidad de desaprobados = {desaprobados}")
    