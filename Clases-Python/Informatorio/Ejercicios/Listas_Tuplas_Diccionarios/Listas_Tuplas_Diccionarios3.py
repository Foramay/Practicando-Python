import os
import platform
import time
"""
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i.
"""
def limpiar_pantalla(x):
    time.sleep(x)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

nombres_especies = ("Jaguar", "Tiburon")

def menu():
    for menu in enumerate(nombres_especies):
        print(f"{menu[0]+1} - {menu[1]}")

#Forma 2
"""while True:
    menu()
    posicion = input("Elegí una opción: ")
    if posicion.isnumeric():
        if int(posicion) > len(nombres_especies):
            print("Opción no válida.")
        else:
            print(f"Hola soy {nombres_especies[int(posicion)-1]}, cuidame.")
    else:
        print("Ingresá un número.")


    limpiar_pantalla(1)"""





#Forma 1
"""for especies in nombres_especies:
    print(f"Hola soy {especies}, cuidame.")
    limpiar_pantalla()"""