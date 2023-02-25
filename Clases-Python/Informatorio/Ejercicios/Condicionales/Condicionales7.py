"""
Desarrolle un programa que permita determinar si un número X ingresado es par o impar.
"""


print("BIENVENIDO.")
numero = input("Ingresá un número: ")

if numero.isalpha():
    print("Ingresá un número válido.")
elif int(numero) % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El numero ingresado es impar.")