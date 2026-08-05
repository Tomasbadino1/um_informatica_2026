#Tienda online - sistema de descuentos
#Se pregunta al usuario si es miembro del club y se usa .upper() para pasar lo que se ingresa a mayusculas.
es_club = input("¿Eres miembro CLUB? (SI/NO): ").upper()

# La función cargar_productos usa un bucle while True para pedir datos hasta que el usuario escriba fin. Se crea una lista producto y se 
#guarda en la lista carrito con .append().
def cargar_productos():
    carrito = []
    while True:
        nombre = input("Producto: ")
        if nombre.lower() == "fin":
            break        
        
        precio = float(input("Precio: "))
        
        producto = [nombre, precio]
        carrito.append(producto)
    return carrito

#Se crea la variable mi_carrito para poder llamar la función.
mi_carrito = cargar_productos()

#Esta función calcula el subtotal creando un acumulador (subtotal) para sumar precios y recorriendo la lista con un bucle for. Se devuelve el subtotal
def calcular_subtotal(productos):
    subtotal = 0
    for producto in productos:
        subtotal += producto[1]
    return subtotal

#Se crea la variable subtotal para llamar a la función con mi_carrito como argumento.
subtotal = calcular_subtotal(mi_carrito)

#La función de calcular_descuento inicializa una lista vacía para los mensajes de descuentos y un acumulador para el descuento total.
#Se usa una variable temporal actual para cada descuento específico y se agrega el texto a la lista con .append(). Al final, la función devuelve 
#el monto total y la lista de mensajes usando el return de múltiples valores.
def calcular_descuento(subtotal, cantidad_productos, es_club):
    mensajes = []
    descuento_total = 0

    if subtotal > 50000:
        actual = subtotal * 0.15
        mensajes.append(f"\nDescuento del 15% por compra superior a $50000: {actual:.2f}")
        descuento_total += actual
    elif subtotal > 20000:
        actual = subtotal * 0.1
        mensajes.append(f"Descuento del 10% por compra superior a $20000: {actual:.2f}")
        descuento_total += actual
    elif subtotal > 10000:
        actual = subtotal * 0.05
        mensajes.append(f"Descuento del 5% por compra superior a $10000: {actual:.2f}")
        descuento_total += actual
    else:
        descuento_total = 0
        
    if es_club == "SI":
        actual = (subtotal - descuento_total) * 0.05
        mensajes.append(f"Descuento del 5% por ser miembro es_club: {actual:.2f}")
        descuento_total += actual
    if cantidad_productos > 5:
        actual = 1000     
        mensajes.append(f"Descuento por cantidad de productos superior a 5: {actual:.2f}")
        descuento_total += actual
        
    return descuento_total, mensajes
       
#Se desempaqueta los dos valores que devuelve la función calcular_descuento en las variables descuento y descuentos_lista. 
descuento, descuentos_lista = calcular_descuento(subtotal, len(mi_carrito), es_club)

#Se calcula el total final restando el descuento acumulado al subtotal
total_final = subtotal - descuento

#Se crea una funcion mostrar_resumen que muestre el recibo de compra. Se utilizan dos bucles for para mostrar la lista de productos y la lista de
#descuentos. Tambien se imprimen con f'strings y formato :.2f para mostrar los demás parametros.
def mostrar_resumen(productos, subtotal, descuento, total, descuentos_lista):
    print("\n===Recibo de compra===")
    for producto in productos:
        print(f"{producto[0]} - {producto[1]}")
    print(f"Subtotal: {subtotal:.2f}")
    for d in descuentos_lista:
        print(d)
    print(f"Descuento aplicado a tu compra: {descuento:.2f}")
    print(f"Total final: {total:.2f}")

#Llamada a la función pasándole todos los datos procesados para mostrar el recibo.
mostrar_resumen(mi_carrito, subtotal, descuento, total_final, descuentos_lista)