"""
Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
"""


numero1 = input("Ingresá el primer número: ")
numero2 = input("Ingresá el segundo número: ")


if numero1.isdigit() and numero2.isdigit():
    if int(numero1) % int(numero2) == 0:
        print("Si es divisor")
    else:
        print("No es divisor")
else:
    print("Ingresá números validos.")