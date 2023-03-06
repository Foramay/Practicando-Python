"""
Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. 
    -El programa no permitirá introducir valores negativos para A y B  
    -Verificar que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
"""

#Creo esta constante para poder hacer el intercambio de valores en caso de que A sea mayor que B
VALOR = 0
SUMA = 0
valor_a = input("Ingresá el primer valor: ")
valor_b = input("Ingresá el segundo valor: ")

if int(valor_a) > int(valor_b):
        VALOR = valor_b
        valor_b = valor_a
        valor_a = VALOR

for i in range(int(valor_a), int(valor_b)+1):
    if int(valor_a) < 0 or int(valor_b) < 0:
        print("No podes ingresar valor negativos.")

    elif i % 5 == 0:
        print(i)
        SUMA = SUMA + i
print(f"La suma es {SUMA}")