#De segundos a hh:mm:ss
#Pidiendo una cantidad de segundos
segundos = int(input("Cantidad de segundos: "))

#Calculando horas, minutos y segundos
horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos = resto % 60 

#Mostrando el resultado mediante f'strings
print(f"{segundos} segundos equivalen a:")
print(f"{horas} horas, {minutos} minutos y {segundos} segundos")