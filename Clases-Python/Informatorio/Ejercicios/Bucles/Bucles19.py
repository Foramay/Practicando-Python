import os
import platform
import time
"""
Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. 
    - Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras, tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).
"""

import os
import platform
import time

TAMAÑO_PIZZA = ("Pequeña", "Mediana", "Grande")
INGREDIENTES = ["Pepinillos", "Champiñones", "Cebollas"]
ingredientes_precio = 50
pizza_precio = 100
precio_total = 0
precio_total_ingredientes = 0
programa = False
def limpiar_pantalla(x):
    time.sleep(x)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def menu_tamaño_pizzas():
    print("Seleciona un tipo de pizza:")
    for menu in enumerate(TAMAÑO_PIZZA):
        print(f"{menu[0]+1} - {menu[1]}")
    print(f"{len(TAMAÑO_PIZZA)+1} - Salir")
def validacion_tipo_pizza(parametro):
    if int(parametro) == len(TAMAÑO_PIZZA)+1:
        return None
    elif int(parametro) > len(TAMAÑO_PIZZA):
        return False
    else:
        return TAMAÑO_PIZZA[int(parametro)-1]
def validacion_ingredientes(parametro):
    if int(parametro) == 1:
        return True
    elif int(parametro) == 2:
        return False
    else:
        return None

print("Bienvenido.")
while True:
    limpiar_pantalla(1)
    cantidad_pizzas = input("¿Cúantas pizzas queres?: ")
    if cantidad_pizzas.isnumeric():
        pizzas = int(cantidad_pizzas)
        break
    else:
        print("Ingresá una cantidad.")

for x in range(1, pizzas+1):
    while True:
        limpiar_pantalla(1)
        menu_tamaño_pizzas()
        tamaño_pizza = input(f"Pizza {x} > ")

        if tamaño_pizza.isnumeric():
            resultado_pizza = validacion_tipo_pizza(tamaño_pizza)
            if resultado_pizza == None:
                programa = True
                break
            elif resultado_pizza == False:
                print("Ingresá una opción válida.")
            else:
                print(f"El tipo de pizza elegido es {resultado_pizza}")
                precio_total = pizzas * pizza_precio
                break
        else:
            print("Selecciona un tamaño de pizza.")
    
    for ingrediente in INGREDIENTES:    
        while programa != True:
            limpiar_pantalla(1)
            print(f"¿Querés agregar {ingrediente} para la pizza {x}?")
            ingredientes = input("1 - Si\n2 - No\n> ")
            if ingredientes.isnumeric():
                resultado_ingredientes = validacion_ingredientes(ingredientes)
                if resultado_ingredientes == None:
                    print("Elegí una opción.")
                elif resultado_ingredientes == False:
                    print(f"No agregaste {ingrediente}.")
                    break
                else:
                    print(f"Agregaste {ingrediente}")
                    precio_total_ingredientes = precio_total_ingredientes + ingredientes_precio
                    break
            else:
                print("Seleccioná una opción.")
    if programa:
        break
print(f"El total a pagar es de ${precio_total+precio_total_ingredientes}.")