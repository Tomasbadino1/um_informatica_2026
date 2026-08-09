# par o impar
# numero = int(input("Ingrese un numero entero: "))
# if numero % 2 == 0:
#   print(f"{numero} es par")
# else:
#    print("es impar")

#comparar usuarios
password = "Tomi1234"
written_password = input("Ingrese contraseña: ")

if written_password == password and len(written_password) >= 8:
    print("INICIANDO SESIÓN...")
else:
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")
