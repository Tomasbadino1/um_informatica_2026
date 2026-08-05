#Calculadora de propina
#Dandole al programa indicaciones para que pueda calcular la cuenta, propina, el total, y cuanto dinero es por persona.
monto_total = float(input("Monto de la cuenta: "))
porcentaje_de_propina = float(input("Porcentaje de propina: "))
cantidad_de_personas = int(input("Cantidad de personas: "))

#Definiendo variables para luego incluirlas en el f'string
propina_total = monto_total * (porcentaje_de_propina /100)
total_a_pagar = monto_total + propina_total
pago_por_persona = total_a_pagar / cantidad_de_personas

#Mostrando resultados mediante f'string del resumen que se debe pagar
print(f"Resumen:")
print(f"Cuenta: {monto_total}")
print(f"Propina: {propina_total}")
print(f"Total: {total_a_pagar}")
print(f"Por persona: {pago_por_persona}")

#¿Qué pasa si la propina es 0%? 
#Si la propina es 0% el monto total sera de 25000, osea, el monto de la cuenta principal.
#¿Y si son 10 personas en lugar de 4?
#Si son 10 personas cada uno pagaria el monto total de la cuenta dividido 10