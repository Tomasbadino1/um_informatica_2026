#Un docstring es un string entre triples comillas al INICIO de la función. Es para vos en 6 meses, para tu equipo, y para Python:
def dias_calurosos(temps, limite=30):
    """Devuelve los días que superaron una temperatura límite."""
    resultado = []
    for t in temps:
        if t > limite:
            resultado.append(t)
    return resultado

# Bonus: help() te muestra el docstring
help(dias_calurosos)
