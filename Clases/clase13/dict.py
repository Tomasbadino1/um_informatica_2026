stock = {"lapices": 50, "gomas": 12, "reglas": 8}
 
print(stock["gomas"])        # 12
 
# Cuidado: una clave que NO existe con [] revienta
#print(stock["mochilas"])     # KeyError: "mochilas"
 
# .get() es la version segura: devuelve None (o un default)
print(stock.get("mochilas"))       # None
print(stock.get("mochilas", 0))    # 0  <- default si no esta
