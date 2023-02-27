"""
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.
"""

print("Bienvenido.")
numero_azar = input("Elegí un número al azar: ")


if numero_azar.isdigit():
    if int(numero_azar) < 74:
        compra = input("Ingresá el monto total de la compra: $")
        if compra.isdigit():
            descuento = int(compra) * 15 // 100
            total = int(compra) - int(descuento)
            print(f"""El descuento es del 15%
El monto total de la compra es de ${float(compra)}
El total a pagar es de ${float(total)}
            """)
        else:
            print("Ingresá el monto de la compra.")
    elif int(numero_azar) >= 74:
        compra = input("Ingresá el monto total de la compra: $")
        if compra.isdigit():
            descuento = int(compra) * 20 // 100
            total = int(compra) - int(descuento)
            print(f"""El descuento es del 20%
El monto total de la compra es de ${float(compra)}
El total a pagar es de ${float(total)}
            """)
        else:
            print("Ingresá el monto de la compra.")
else:
    print("Elegí un número al azar.")