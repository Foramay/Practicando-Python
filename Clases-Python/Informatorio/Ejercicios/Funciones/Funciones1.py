"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
"""


def relacion(a, b):
    if int(a) > int(b):
        print("Ciudad 1")
    elif int(a) < int(b):
        print("Ciudadd 2")
    else:
        print("Ciudad 1 y Ciudad 2")


ciudad_1 = input("Ingresá la cantidad de toneladas de la ciudad 1: ")
ciudad_2 = input("Ingresá la cantidad de toneladas de la ciudad 2: ")


relacion(ciudad_1, ciudad_2)