"""
Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
"""
print("Bienvenido.")
numero1 = input("Ingresá un número: ")
numero2 = input("Ingresá otro número: ")


if numero1.isdigit() and numero2.isdigit():
    if numero1 == numero2:
        operacion = "multiplicación"
        resultado = int(numero1) * int(numero2)
    elif numero1 > numero2:
        operacion = "resta"
        resultado = int(numero1) - int(numero2)
    else:
        operacion = "suma"
        resultado = int(numero1) + int(numero2)
    print(f"""La operacion que se ejecutó es una {operacion}.
El resultado de la operación es {resultado}
    """)
else:
    print("Ingresá números para hacer la operación.")