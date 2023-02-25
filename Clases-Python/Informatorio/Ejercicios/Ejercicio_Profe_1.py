"""
Ejercicio 1
Escribir un programa en Python que realice la suma de dos números ingresados por el usuario, y al final emita un mensaje con el resultado.
"""


resultado1 = input ("Escriba el primer número: ")
resultado2 = input ("Escriba el segundo número: ")

if resultado1.isdigit() and resultado2.isdigit():
    suma = int(resultado1) + int(resultado2)
    print(f"""El primer número ingresado es {resultado1} y el segundo es {resultado2}.
La suma de estos números es {suma}""")
else:
    print("Los valores ingresados no son numeros.")
