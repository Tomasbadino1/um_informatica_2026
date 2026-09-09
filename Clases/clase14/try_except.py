try:
    edad = int(input("Edad: "))
    print("El año que viene tenés", edad + 1)
except ValueError:
    print("Eso no es un número válido.")


try:
    n = int(input("Número: "))
except ValueError:
    print("No era un número.")     # SI hubo error
else:
    print("Perfecto:", n)          # si NO hubo error
finally:
    print("Listo, terminé.")       # SIEMPRE, pase lo que pase

try:
    resultado = 10 / 0
except ValueError:
    print("Dato inválido")
except ZeroDivisionError:
    print("No se puede dividir por cero")   # <- entra acá
