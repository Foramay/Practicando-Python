"""
Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.
"""

print("Bienvenido.")

suma = 0
while True:
    producto = input("Ingresá el producto: ")
    precio_producto = input(f"Ingresá el precio del {producto}: $")
    cantidad_producto = input(f"Ingresá la cantidad de {producto}: ")

    suma = int(suma) + int(precio_producto) * int(cantidad_producto)

    seguir = input("Desea agregar más productos?: si/no ")
    if seguir.lower() == "no":
        break
print(f"El total a pagar es ${suma}")