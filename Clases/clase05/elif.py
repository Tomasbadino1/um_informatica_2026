nota = int(input("Ingrese una nota: "))
asistencia = int(input("Ingrese porcentaje de asistencia (de 0 a 100%): "))
if nota == 10:
    print("Sobresaliente")
    if asistencia >= 90:
        print("Promocionado")
        
elif 9 >= nota >= 8:   
    print("Muy bien")
    if asistencia >= 90:
        print("Promocionado")
        
elif 7 >= nota >= 6:
    print("Aprobado")
    
else:
    print("Desaprobado")

#Operador Ternario
condicion = "Promocionado" if ( nota >= 8 and asistencia >= 80 ) else "Rinde Final"     
