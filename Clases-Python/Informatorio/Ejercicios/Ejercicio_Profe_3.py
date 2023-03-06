"""
Ejercicio 2:
Realizar un programa en python, que solicite el ingreso de numeros enteros, teniendo en cuenta lo siguiente: 
    -Si se ingresa un valor distinto a un numero entero positivo deberá mostrar un mensaje de error y solicitar nuevamente el ingreso de datos.
    -El programa finalizara cuando se ingrese fin
Al finalizar informar:
    -Cantidad de números validos
    -Cantidad de errores producidos
    -Suma total de todos los números ingresados
    -Promedio de numeros ingresados
"""
numeros_validos = 0
errores = 0
suma_total_numeros = 0
promedio = 0
contador = 0
print("Bienvenido.")

while True:
    numero = input("Ingresá un número: ")
    if numero == "fin":
        break
    if not numero.isalpha():
        contador = contador + 1
        suma_total_numeros = int(suma_total_numeros) + int(numero)
        promedio = int(suma_total_numeros) / int(contador)
        if int(numero) > 0:
            print("Es un número positivo")
            numeros_validos = numeros_validos + 1 
        elif int(numero) < 0:
            print("Es un número negativo.")
            errores = errores + 1
        else:
            print("El número es 0")
    else:
        print("Ingresá un número.")
        errores = errores + 1

print(f"""
La cantidad de números válidos es de {numeros_validos}.
La cantidad de errores producidos es de {errores}.
El total de todos los números es de {suma_total_numeros}.
Y el promedio es de {promedio}.
""")