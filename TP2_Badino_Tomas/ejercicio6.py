#Generador de tablas y patrones
#Para este ejercicio se debe realizar 4 funciones, la primera es una tabla de multiplicar que se realizó con un bucle for i en un rango desde el 1 
# al 11 ya que este el segundo parametro que se pone es el fin y no es inclusivo, por lo que llegaria del 1 al 10. Se creó una variable resultado
# que es igual al numero por el que queremos multiplicar todo el rango i (1-10). Como resultado se imprime con un f'string.
def tabla_multiplicar(n):
    for i in range(1,11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
        
#La segunda función es la tabla completa de un numero multiplicado por si mismo. Primero el primer bucle for para la fila con rango que empieza
#en 1 y termina en n+1 ya que como el segundo parametro es excluyente se le suma 1 para incluirlo. Se realiza el mismo bucle for para la columna
# con el mismo rango, para finalizar imprimiendo la tabla con f'string donde se multiplica f * c porque es la logica de N X N. El \t es para un
#espacio entre cada numero y el end= para"" para imprimir sin salto de linea y print() solo para terminar la línea.
def tabla_completa(n):
    for f in range(1, n+1):
        for c in range(1, n+1):
            print(f"{f * c}\t", end="")
        print()

#La tercer funcion es la de triángulo, donde se usa dos bucles anidados: f para fila, con rango 1, altura+1 para incluir el numero que se ingresa. 
#Para columna es c, con rango de f porque la cantidad de columnas depende de la cantidad de filas. Se imprime con * y con un end=.
def triangulo(altura):
    for f in range(1, altura+1):
        for c in range(f):
            print("*", end="")
        print()

#La cuarta es la de triángulo invertido, es similar a la tercer funcion, pero cambia en el caso de las filas, ya que la cantidad de asteriscos 
#en la primer fila sería la altura que se ingresa. El 0 es el fin (para poder incluir al 1) y el -1 indica que se resta 1 en cada vuelta.
def triangulo_invertido(altura):
    for f in range(altura, 0, -1):
        for c in range(f):
            print("*", end="")
        print()
        
#Funciones:
tabla_multiplicar(3)
tabla_completa(4)
triangulo(4)
triangulo_invertido(4)