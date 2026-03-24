# Función: texto → base 10 → binario (cifrado)
def cifrar(texto):
    lista_decimal = []
    lista_binario = []

    for caracter in texto:
        valor_decimal = ord(caracter)   # Base 10 (ASCII)
        lista_decimal.append(valor_decimal)

        valor_binario = format(valor_decimal, '08b')  # A binario
        lista_binario.append(valor_binario)

    return lista_decimal, lista_binario


# Función: binario → base 10 → texto (descifrado)
def descifrar(lista_binario):
    texto = ""

    for b in lista_binario:
        valor_decimal = int(b, 2)  # Binario a base 10
        texto += chr(valor_decimal)  # Base 10 a carácter

    return texto


# Programa principal (secuencial)
def main():
    cadena = input("Ingrese una cadena de texto: ")

    # Cifrado
    decimales, binarios = cifrar(cadena)

    print("\nValores en base 10 (ASCII):")
    print(decimales)

    print("\nValores en binario:")
    print(" ".join(binarios))

    # Descifrado
    texto_recuperado = descifrar(binarios)

    print("\nTexto descifrado:")
    print(texto_recuperado)


# Ejecutar programa
main()