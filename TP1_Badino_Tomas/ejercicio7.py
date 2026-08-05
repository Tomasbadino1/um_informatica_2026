#Calculadora de IMC con clasificación
#Pidiendole al usuario que ingrese peso y altura
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

#Definiendo la formula de Indice de Masa Corporal (IMC)
imc = peso / (altura ** 2)

#Clasificando el IMC mediante comparaciones
bajo_peso = imc < 18.5
peso_normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and (imc < 30)
obesidad = imc >= 30

#Mostrando resultados mediante f'string del indice de masa corporal y que me lo indique con valores booleanos (el True sera el IMC)
print("Resultados:")
print(f"IMC = {imc:.2f}")
print(f"Bajo peso: {bajo_peso}")
print(f"Peso normal: {peso_normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad: {obesidad}")