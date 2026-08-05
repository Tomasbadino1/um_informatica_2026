#¿Cuánto tiempo viví?
#Pidiendo edad de la persona en años
edad = int(input("¿Cuantos años tenes? "))

#Calculando el tiempo vivido aproximado
dias = edad * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
latidos_del_corazon = minutos * 70

#Mostrando resultados mediante f'strings
print(f"En {edad} años aproximadamente viviste:")
print(f"Dias: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
print(f"Latidos por minuto: {latidos_del_corazon}")