#Agenda de contactos

agenda = {
    "Ana": "351-111",
    "Beto": "351-222",
    "Caro": "351-333",
}

    
while True:
    print("Menu de contactos: \n1. Agregar un contacto nuevo: \n2. Preguntar por contacto y su numero: \n3. Lista de contactos: ")
    opciones = int(input("Ingrese una opción: "))
    if opciones == 1:
        nombre = input("Nombre: ")
        numero = int(input("Numero: "))
        agenda[nombre] = numero

    elif opciones == 2:
        for contacto in agenda:
            nombre = input("Nombre: ")
            telefono = agenda.get(nombre, "no existe ese contacto")
            print(f"{nombre}: {telefono}")

    elif opciones == 3: 
        print("-Agenda-")
        for contacto, telefono in agenda.items():
            print(f"{contacto}: {telefono}")

# agenda["Nico"] = "351-67"

#     for contacto in agenda:
#         nombre = input("Nombre: ")
#         telefono = agenda.get(nombre, "no existe ese contacto")
#         print(f"{nombre}: {telefono}")

#     print("-Agenda-")
#     for contacto, telefono in agenda.items():
#         print(f"{contacto}: {telefono}")