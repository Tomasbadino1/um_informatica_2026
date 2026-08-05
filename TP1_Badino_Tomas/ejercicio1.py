#Conversor de kilómetros a millas
#Pidiendo al usuario que ingrese un valor de kilometros.
km = float(input("Ingresá kilómetros: "))
km_a_millas = (km / 1.60934)

#Mostrando mediante f'strings la conversion de kilometros a millas y con un especificador de decimales despues de la coma.
print(f"{km:.0f} kilometros equivalen a {km_a_millas:.2f} millas")

#Pidiendo al usuario que ingrese un valor de millas
milla = float(input("Ingresá millas: "))
millas_a_km = (milla * 1.60934)

#Mostrando mediante f'strings la conversion de kilometros a millas y con un especificador de decimales despues de la coma.
print(f"{milla:.0f} millas equivalen a {millas_a_km:.2f} kilometros")