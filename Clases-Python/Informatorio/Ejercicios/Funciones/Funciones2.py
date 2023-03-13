"""
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. 
    - Luego la función debe devolver dos listas ordenadas. 
        - La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""
import os
import platform
def limpiar_pantalla():
    if platform.system() == "Windows":
            os.system("cls")
    else:
        os.system("clear")
#Creo una lista para guardar la cantidad de arboles ingresados
lista_cantidad_arboles = []
#En esta lista guardo todos los arboles plantados en una ciudad que superen los 100 
nueva_lista = []
CANTIDAD_CIUDADES = 0

#Esta funcion recibe como parametro la cantidad de arboles ingresados por el usuario
def separar_lista(cantidad_arboles):
    #Agrego la cantidad de arboles ingresados por el usuario a la lista
    lista_cantidad_arboles.append(cantidad_arboles)

    #Itero por cada elemento de la lista
    for i in lista_cantidad_arboles:    
        if int(i) > 100:
            #Si se supera los 100 arboles, se agrega la cantidad a la nueva lista
            nueva_lista.append(i)
            #Y aca se elimina de la lista
            lista_cantidad_arboles.remove(i)


print("Bienvenido.")

empezar = input("Querés agregar arboles: si/no ")
while empezar.lower() == "si" and empezar.lower() != "no":
    limpiar_pantalla()
    CANTIDAD_CIUDADES = CANTIDAD_CIUDADES + 1
    cantidad_arboles = input("Agrega la cantidad de arboles: ")
    

    #Aca hago las validaciones
    if cantidad_arboles.isdigit():
        separar_lista(cantidad_arboles)
    else:
        print("Ingresá un número valido.")

    seguir = input("Querés agregar otro arbol?: si/no ")
    if seguir.lower() != "si" and seguir.lower() == "no":
        break
#Y por ultimo ordeno las 2 listas
lista_cantidad_arboles.sort()
nueva_lista.sort()
limpiar_pantalla()
print(f"La cantidad de ciudades que plantaron arboles es de {CANTIDAD_CIUDADES}.\nLa lista que superan no los 100 {lista_cantidad_arboles}.\nY los que superan los 100 {nueva_lista}")