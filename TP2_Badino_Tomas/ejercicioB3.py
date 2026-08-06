#Codificador César
def cifrar(texto, n):
    cifrado = []
    for letra in texto:
        if letra.isupper():
            codigo = ord(letra) - ord("A")
            nuevo_codigo = (codigo + n) % 26 + ord("A")
            cifrado.append(chr(nuevo_codigo))
            
        elif letra.islower():
            codigo = ord(letra) - ord("a")
            nuevo_codigo = (codigo + n) % 26 + ord("a")
            cifrado.append(chr(nuevo_codigo))
        else:
            cifrado.append(letra)
    return "".join(cifrado)


def descifrar(texto, n):
    descifrado = []
    for letra in texto:
        if letra.isupper():
            codigo = ord(letra) - ord("A")
            nuevo_codigo = (codigo - n) % 26 + ord("A")
            descifrado.append(chr(nuevo_codigo))
            
        elif letra.islower():
            codigo = ord(letra) - ord("a")
            nuevo_codigo = (codigo - n) % 26 + ord("a")
            descifrado.append(chr(nuevo_codigo))
        else:
            descifrado.append(letra)
    return "".join(descifrado)

print(cifrar("Hola mundo", 3))
print(descifrar("def ABC", 3))