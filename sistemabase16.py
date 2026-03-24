# Función: texto → base 16 → binario (cifrado)
def cifrar(texto):
    lista_hex = []
    lista_binario = []

    for caracter in texto:
        valor_hex = format(ord(caracter), '02x')  # ASCII a hexadecimal
        lista_hex.append(valor_hex)

        valor_binario = format(int(valor_hex, 16), '08b')  # Hex a binario
        lista_binario.append(valor_binario)

    return lista_hex, lista_binario


# Función: binario → base 16 → texto (descifrado)
def descifrar(lista_binario):
    texto = ""

    for b in lista_binario:
        valor_hex = format(int(b, 2), '02x')  # Binario a hexadecimal
        valor_decimal = int(valor_hex, 16)   # Hex a decimal
        texto += chr(valor_decimal)          # Decimal a carácter

    return texto


# Programa principal (secuencial)
def main():
    cadena = input("Ingrese una cadena de texto: ")

    # Cifrado
    hexadecimales, binarios = cifrar(cadena)

    print("\nValores en base 16 (hexadecimal):")
    print(hexadecimales)

    print("\nValores en binario:")
    print(" ".join(binarios))

    # Descifrado
    texto_recuperado = descifrar(binarios)

    print("\nTexto descifrado:")
    print(texto_recuperado)


# Ejecutar programa
main()