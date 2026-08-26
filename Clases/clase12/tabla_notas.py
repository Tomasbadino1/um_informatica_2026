#Promedio por alumno
notas = [[8, 7, 9],    # Ana
         [5, 6, 4],    # Beto
         [10, 9, 8]]   # Caro
nombres = ["Ana", "Beto", "Caro"]

for i in range(len(notas)):        
    fila = notas[i]
    promedio = sum(fila) / len(fila)
    if promedio >= 6: estado = "Promocionado" 
    else:
        estado = "Sin promocion"
    print(f"Alumno: {nombres[i]} - Promedio: {promedio} - Estado: {estado}")

    
    
    
