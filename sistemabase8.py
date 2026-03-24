# Función: texto → base 8 → binario (cifrado)
def cifrar(texto):
    lista_octal = []
    lista_binario = []

    for caracter in texto:
        valor_octal = format(ord(caracter), '03o')  # ASCII a octal (base 8)
        lista_octal.append(valor_octal)

        valor_binario = format(int(valor_octal, 8), '08b')  # Octal a binario
        lista_binario.append(valor_binario)

    return lista_octal, lista_binario


# Función: binario → base 8 → texto (descifrado)
def descifrar(lista_binario):
    texto = ""

    for b in lista_binario:
        valor_octal = format(int(b, 2), '03o')  # Binario a octal
        valor_decimal = int(valor_octal, 8)     # Octal a decimal
        texto += chr(valor_decimal)             # Decimal a carácter

    return texto


# Programa principal (secuencial)
def main():
    cadena = input("Ingrese una cadena de texto: ")

    # Cifrado
    octales, binarios = cifrar(cadena)

    print("\nValores en base 8 (octal):")
    print(octales)

    print("\nValores en binario:")
    print(" ".join(binarios))

    # Descifrado
    texto_recuperado = descifrar(binarios)

    print("\nTexto descifrado:")
    print(texto_recuperado)


# Ejecutar programa
main()