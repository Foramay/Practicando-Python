"""
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.
"""

lista_elementos = ["Bolsa de plastico", "Botella Pet", "Envase Tetrabik", "Chicle"]


def obtener_resultado(opcion):
    if int(opcion) == 1:
        return 150
    elif int(opcion) == 2:
        return 1000
    elif int(opcion) == 3:
        return 30
    elif int(opcion) == 4:
        return 5
    return None


def menu():
    print("Seleccioná una opción:")
    for elemento in enumerate(lista_elementos):
        print(f"{elemento[0]+1} - {elemento[1].capitalize()}")
    print(f"{len(lista_elementos) + 1} - Salir")

print("Bienvenido")

while True:

    menu()
    elemento_seleccionado = input("> ")

    guardar_resultado = obtener_resultado(elemento_seleccionado)
    if int(elemento_seleccionado) == len(lista_elementos) + 1:
        print("Fin del programa.")
        break

    print(f"El elemento seleccionado es {lista_elementos[int(elemento_seleccionado)-1]} y tarda {guardar_resultado} años en degradarse.")
    

    input("Una tecla para seguir.")