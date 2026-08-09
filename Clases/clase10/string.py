# # Registro de usuario
# email_raw = input("Email: ")          # "  Ana.Garcia@UM.EDU.AR  \n"

# # Limpieza paso a paso:
# email = email_raw.strip()                # saca espacios y \n bordes
# email = email.lower()                    # pasa a minúscula

# # Validación simple
# if "@" in email and "." in email:
#     print(f"Email registrado: {email}")
# else:
#     print("Email inválido")



# texto = input("Notas separadas por coma: ")
# # usuario tipea: " 8, 6 , 9,4, 10 "

# partes = texto.split(",")                # [' 8', ' 6 ', ' 9', '4', ' 10 ']
# notas = []
# for p in partes:
#     notas.append(int(p.strip()))         # limpia y convierte a int

# print(notas)                            # [8, 6, 9, 4, 10]
# print(f"Promedio: {sum(notas)/len(notas):.2f}") # 7.40



# Imprimir tabla de notas alineada
alumnos = [
    ("Ana", 8.5),
    ("Carlos", 7),
    ("Maximiliano", 9.25)
]

for nombre, nota in alumnos:
    print(f"{nombre:<15} | {nota:>15.2f}")