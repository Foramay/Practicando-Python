"""
Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. El ciclo debe finalizar cuando el usuario ingresa 0.
"""

while True:
    numero = input("Ingesá un número: ")
    if numero.isdigit():
        if int(numero) == 0:
            break
        elif int(numero) % 2 == 0:
            print("Es par.")
        else:
            print("Es impar")
    else:
        print("Ingresá un número válido.")
print("Fin del programa.")

