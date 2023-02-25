import os
"""
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.
"""

print("Ingresá el nombre del barrio:")
nombre_barrio = input(">")
print("Ingresá la ubicación: Centrico / No Centrico")
ubicacion = input("> ")
os.system("cls")

if not nombre_barrio.isdigit() and not ubicacion.isdigit():
    if (nombre_barrio.lower() < "m" and ubicacion.lower() == "centrico") or (nombre_barrio.lower() > "m" and ubicacion.lower() == "no centrico"):
        seccion = "A"
    else:
        seccion = "B"
    print(f"Perteneces a la sección {seccion}")
else:
    print("Error. Debés seguir las consignas.")