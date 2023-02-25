"""
Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
"""


numero = input("Ingresá 3 números: ")


if len(numero) == 3 and numero.isdigit():
    if numero[0] > numero[1] and numero[0] > numero[2]:
        print("El primer número es mayor a los otros 2.")
    else:
        print("El primer número no es mayor a algunos de los otros dos.")
else:
    print("Ingresá 3 digitos.")