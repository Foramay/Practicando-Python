"""
Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
"""


numero1 = input("Ingesá el primer número: ")
numero2 = input("Ingesá el segundo número: ")
numero3 = input("Ingesá el tercer número: ")


if numero1 > numero2 and numero2 > numero3:
    print(f"Elif 1 {numero1, numero2, numero3}")
elif numero2 > numero1 and numero1 > numero3:
    print(f"Elif 2 {numero2, numero1, numero3}")
elif numero3 > numero2 and numero2 > numero1:
    print(f"Elif 3 {numero3, numero2, numero1}")
elif numero2 > numero3 and numero3 > numero1:
    print(f"Elif 4 {numero2, numero3, numero1}")
elif numero1 > numero3 and numero3 > numero2:
    print(f"Elif 5 {numero1, numero3, numero2}")
elif numero3 > numero1 and numero1 > numero2:
    print(f"Elif 6 {numero3, numero1, numero2}")
else:
    print("Todos los numeros son iguales")