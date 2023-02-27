"""
Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).
"""



nombre_articulo = input("Ingresá el nombre del artículo: ")
precio_original = input(f"Ingresá el precio de {nombre_articulo}: $")
clave_descuento = input("Ingresá la clave de descuento: ")


if clave_descuento == "01":
    clave_1 = int(precio_original) * 10 // 100
    total_descuento = int(precio_original) - int(clave_1)
    print(f"El total a pagar por el artículo {nombre_articulo} es de ${total_descuento}")
elif clave_descuento == "02":
    clave_2 = int(precio_original) * 20 // 100
    total_descuento = int(precio_original) - int(clave_2)
    print(f"El total a pagar por el artículo {nombre_articulo} es de ${total_descuento}")
else:
    print(f"""No hay descuento para este artículo.
El total a pagar es de ${precio_original}
    """) 