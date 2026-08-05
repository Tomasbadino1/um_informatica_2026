#Conversor de temperatura (°C ↔ °F)
#Pidiendo al usuario que ingrese una temperatura °C
celcius = float(input("Temperatura en °C: "))
celsius_a_fahrenheit = celcius * 9/5 + 32

#Mostrando mediante f'string la conversion de celsius a fahrenheit.
print(f"{celcius}°C equivalen a {celsius_a_fahrenheit}°F")

#Pidiendo al usuario que ingrese una temperatura °F
fahrenheit = float(input("Temperatura en °F: "))
fahrenheit_a_celsius = (fahrenheit - 32) * 5/9

#Mostrando mediante f'string la conversion de fahrenheit a celsius y con un especificador de decimales despues de la coma.
print(f"{fahrenheit}°F equivalen a {fahrenheit_a_celsius:.2f}°C")