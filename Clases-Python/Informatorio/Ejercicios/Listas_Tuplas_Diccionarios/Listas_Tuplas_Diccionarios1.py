"""
- Crea una tupla con los factores que más afectan a los mares. 
- Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""


factores_que_afectan_a_mares = ("Las aguas residuales", "Las sustancias químicas tóxicas", "Las aguas pluviales", "El vertido de plásticos.")
print("Bienvenido.")

def obtener_resultado(opcion):
    if int(opcion) == 1:
        return 0
    elif int(opcion) == 2:
        return 1
    elif int(opcion) == 3:
        return 2
    elif int(opcion) == 4:
        return 3
    return None

while True:
    numeros = input(f"Ingresá un número del 1 al {len(factores_que_afectan_a_mares)}: ")

    if numeros.isnumeric():
        guardar_resultado = obtener_resultado(numeros)
        if guardar_resultado == None:
            print(f"Ingresá un número valido del 1 al {len(factores_que_afectan_a_mares)}.")
        else:
            print(f"El elemento elegido es {factores_que_afectan_a_mares[int(numeros)-1]}")
    else:
        print("Ingresá un número.")

    volver_jugar = input("¿Querés volver a jugar?: si/no ")

    if volver_jugar.lower() == "no" or volver_jugar.lower() != "si":
        print("Fin del juego.")
        break