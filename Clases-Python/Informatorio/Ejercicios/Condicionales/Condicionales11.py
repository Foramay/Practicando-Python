"""
Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
"""


compra_cliente = input("¿Cúanto es el importe a pagar?: $")

if compra_cliente.isdigit():
    if int(compra_cliente) > 1000:
        total = int(compra_cliente) * 15 / 100
    else:
        print("No tenés ningún descuento.")
        total = compra_cliente
else:
    print("El importe no es válido.")

print(f"El total a pagar es de ${total}")