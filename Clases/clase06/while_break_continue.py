# Pedir números hasta que escriban 0
total = 0

while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    total += n

print(f"Total: {total}")
