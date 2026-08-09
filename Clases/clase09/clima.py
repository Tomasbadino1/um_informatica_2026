temperaturas = [28, 32, 35, 29, 31, 33, 27]

def temperatura_promedio(temps):
    total = 0
    for temp in temps: 
        total += temp
    return total / len(temps)

def dias_calurosos(temps, limite=30):
    dias = []
    for t in temps: 
        if t > limite: dias.append(t)
    return dias
    
def clasificar_dia(temps):
    if temps < 20: return "Frio"
        
    elif temps < 30: return "Templado"
        
    elif temps >= 30: return "Caluroso"
        
print(f"Promedio: {temperatura_promedio(temperaturas)} °C")
print(f"Dias calurosos: {dias_calurosos(temperaturas)}")
print(f"Como esta el dia: {clasificar_dia(temperaturas[-1])}")