# filas, columnas = 3, 3
# matriz = []
# for f in range(filas):
#     fila = [0] * columnas      # [0, 0, 0]
#     matriz.append(fila)
# print(matriz)   


matriz = [[1, 2, 3],
          [4, 5, 6, 5]]

total = 0

for fila in matriz:
    for columna in fila:
        total += columna
print(total)

a = [0] * 5
print(a)

matriz = [[1, 2, 3],
          [4, 5, 6]]
 
for fila in matriz:          # fila es una lista completa
    for valor in fila:       # valor es cada numero
        print(valor, end=" ")
    print()                  
    
for f in range(len(matriz)):           # f = indice de fila
    for c in range(len(matriz[f])):    # c = indice de columna
        print(f"[{f}][{c}] = {matriz[f][c]}")


matriz = [[1, 2, 3],
          [4, 5, 6]]
 
for c in range(len(matriz[0])):    # por cada columna
    suma = 0
    for f in range(len(matriz)):   # recorro las filas
        suma = suma + matriz[f][c]
    print(f"Columna {c}: {suma}")