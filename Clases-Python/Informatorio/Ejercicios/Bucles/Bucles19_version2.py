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
programa = False
costos_ingredientes = 0
costo_pizzas = 0
TAMAÑO_PIZZA = [
    {"tamaño_pizza": "Pequeño", "costo": 100},
    {"tamaño_pizza": "Mediano", "costo": 200},
    {"tamaño_pizza": "Grande", "costo": 300},
    {"tamaño_pizza": "Extra Grande", "costo": 400}
]

INGREDIENTES = [
    {"ingrediente": "Cebolla", "costo": 50},
    {"ingrediente": "Pepinillos", "costo": 150},
    {"ingrediente": "Tomate", "costo": 50},
    {"ingrediente": "Atún", "costo": 150}
]
def limpiar_pantalla(x):
    time.sleep(x)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu_pizzas():
    print(f"Elegí el tamaño de la pizza {x}.")
    cont = 1
    for menu in TAMAÑO_PIZZA:
        print(f"{cont} - {menu['tamaño_pizza']}")
        cont += 1
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
    cantidad_pizzas = input("¿Cúantas pizzas querés?: ")
    if cantidad_pizzas.isnumeric():
        pizzas = int(cantidad_pizzas)
        break
    else:
        print("Elegí la cantidad de pizzas.")
        limpiar_pantalla(1)

for x in range(1, pizzas+1):
    while True:
        limpiar_pantalla(1)
        menu_pizzas()
        tamaño_pizza = input("> ")
        if tamaño_pizza.isnumeric():
            guardar_resultado_tamaño_pizza = validacion_tipo_pizza(tamaño_pizza)
            if guardar_resultado_tamaño_pizza == None:
                programa = True
                break
            elif guardar_resultado_tamaño_pizza == False:
                print("Ingresá una opción válida.")
            else:
                print(f"El tipo de pizza elegido es {guardar_resultado_tamaño_pizza['tamaño_pizza']}")
                costo_pizzas += guardar_resultado_tamaño_pizza['costo']
                break
        else:
            print("Elegí un tamaño.")
    for menu in INGREDIENTES:
        while programa != True:
            limpiar_pantalla(1)
            print(f"Elegí ingredientes para la pizza {x}.")
            print(f"¿Querés agregar {menu['ingrediente']}?")
            ingrediente = input(f"1 - Si\n2 - No\n> ")
            
            if ingrediente.isnumeric():
                guardar_resultado_ingredientes = validacion_ingredientes(ingrediente)
                if guardar_resultado_ingredientes == None:
                    print("Elegí una opción.")
                elif guardar_resultado_ingredientes == False:
                    print(f"No agregaste {menu['ingrediente']}.")
                    break
                else:
                    print(f"Agregaste {menu['ingrediente']}")
                    costos_ingredientes += menu['costo']
                    break
            else:
                print("Elegí una opción.")
    
print(f"""
El total de los ingredientes agregados es ${costos_ingredientes}.
El total por la pizzas son ${costo_pizzas}.
El total a pagar ${costo_pizzas+costos_ingredientes}
""")