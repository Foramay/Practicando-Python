"""
Ejercicio 4: Mediana de tres valores

Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. Incluya un programa principal que lea tres valores del usuario y muestre su mediana.



Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática.
"""

LISTA = []
cont = 1
def obtener_valor_medio(*args):
    #*args sería un tupla
    #Iteramos por cada elemento de la tupla
    for numero in args:
        #Y agregamos el elemento a una lista
        LISTA.append(numero)
    #Acá ordenamos la lista de forma ascendente con el metodo sort()
    LISTA.sort()
    #Y finalmente mostramos por pantalla el resultado del medio ingresando al elemento
    print(f"El número intermedio es {LISTA[cont]}")  

obtener_valor_medio(109, 19, 5)