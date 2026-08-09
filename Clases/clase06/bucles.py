total = 0                            # paso 1: inicializar
for i in range(1, 101):
    total += i                       # paso 2: acumular en cada vuelta
print(f"Suma 1-100: {total}") 


# aprobados = 0
# desaprobados = 0
# excelentes = 0

# for i in range(10):
#     nota = float(input(f"Nota {i+1}: "))
#     if nota >= 9:
#         excelentes += 1
#     if nota >= 6:
#         aprobados += 1
#     else:
#         desaprobados += 1
        
        
# Pedir edad hasta que sea válida (entre 1 y 120)
edad = int(input("Edad: "))

while edad < 1 or edad > 120:
    print("Edad inválida. Tiene que estar entre 1 y 120.")
    edad = int(input("Edad: "))

print(f"Tu edad es {edad}")
