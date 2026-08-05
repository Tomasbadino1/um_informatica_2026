#Validador de contraseñas
#Creando una funcion que valide contraseñas. Primero se creó 5 variables booleanas en False en el que se tornan en True en el momento que la 
#contraseña cumple con la condicion del minimo de caracteres o si alguno de estos caracteres tiene alguna de las demás condiciones, osea, letra
#mayúscula, minúscula, digito y carácter especial. También se creo una variable errores con una lista vacia, en el que debajo de esta se puso 
#5 if para comprobar que si NO tiene alguna de las variables booleanas se agrega a la lista de errores.
def validar_password(pwd):
    tiene_caracteres = False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    caract_especial = False    
    if len(pwd) >= 8: tiene_caracteres = True
    for c in pwd:
        if c.isupper(): tiene_mayuscula = True
        if c.islower(): tiene_minuscula = True
        if c.isdigit(): tiene_digito = True
        if c in "!@#$%&*?": caract_especial = True
    errores = []
    if not tiene_caracteres: errores.append("- Al menos 8 caracteres")
    if not tiene_mayuscula: errores.append("- Al menos una letra mayúscula")
    if not tiene_minuscula: errores.append("- Al menos una letra minúscula")
    if not tiene_digito: errores.append("- Al menos un dígito")
    if not caract_especial: errores.append("- Al menos un carácter especial")
    return errores
    

#Pidiendole al usuario que ingrese una contraseña
pwd = input("Ingrese la contraseña: ")


errores_encontrados = validar_password(pwd)

#Mostrando validación de contraseña
#Contraseña segura: si la cantidad de errores, osea, el largo, es igual a 0:
if len(errores_encontrados) == 0:
    print("Contraseña SEGURA")

#Contraseña insegura: si hay algun error, se hara una lista con la cantidad de errores
else:
    print("Contraseña INSEGURA. Le falta:")
    for error in errores_encontrados:
        print(error)