"""
Determinar el número mayor de 10 números ingresados.
"""


numero_mayor = 0
print("Bienvenido")
for i in range(10):
    numero = input("Ingresá el número: ")
    if int(numero) > int(numero_mayor):
        numero_mayor = int(numero)
print( f"El número mayor es {numero_mayor}")