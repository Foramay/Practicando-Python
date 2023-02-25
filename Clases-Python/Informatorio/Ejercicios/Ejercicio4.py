"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

numero = input("Ingresa un numero: ")


if int(numero) % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")