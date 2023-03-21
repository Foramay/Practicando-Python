import os
import platform
import time
"""
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""
def limpiar_pantalla():
    time.sleep(1)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

conocimiento_personas = []
print("Bienvenido.")

while True:
    limpiar_pantalla()
    personas = input("¿Cúanto conoces de contaminación del 1 al 10?: ")

    if personas.isnumeric():
        if int(personas) < 11:
            print(f"Tu conocimiento de contaminación es de {personas}")
            conocimiento_personas.append(personas)
        else:
            print("Ingresá un valor del 1 al 10.")
    else:
        print("Ingresá un número.")

    conocimiento_personas.sort()
    
    agregar_persona = input("¿Querés ingresar otra persona?: si/no ")

    if agregar_persona.lower() == "no" or agregar_persona.lower() != "si":
        print("Fin del programa.")
        break

print(f"Conocimientos ordenados de menor a mayor {conocimiento_personas}")