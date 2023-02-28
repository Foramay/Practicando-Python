"""
Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos).
"""

lado1 = input("Ingresá la longitud del primer lado: ")
lado2 = input("Ingresá la longitud del segundo lado: ")
lado3 = input("Ingresá la longitud del tercer lado: ")


if lado1.isdigit() and lado2.isdigit() and lado3.isdigit():
    if (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado1 == lado3 and lado1 != lado2):
        print("2 lados iguales.")
    elif lado1 != lado2 and lado2 != lado3:
        print("3 lados distintos.")
    else:
        print("Los 3 lados iguales.")
else:
    print("Ingresá números válidos.")