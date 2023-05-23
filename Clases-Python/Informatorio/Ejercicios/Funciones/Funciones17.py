import os
import platform
import time
"""
Ejercicio 15: Verificar una contraseña

En este ejercicio escribirá una función que determina si una contraseña es buena o no. 
-Definiremos como una buena contraseña aquella que tenga una longitud de al menos 8 caracteres y contenga al menos una letra mayúscula, al menos una letra minúscula y al menos un número. 
-Su función debe devolver verdadero si la contraseña que se le pasó, como único parámetro, es buena, de lo contrario debería devolver falso. 
-Incluya un programa principal que lea una contraseña del usuario e informe si es buena o no.
"""

#Creo listas para despúes iterar sobre ellas en sus respectivas funciones
LETRAS_ABECEDARIO_MAYUSCULAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LETRAS_ABECEDARIO_MINUSCULAS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUMEROS_LISTA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def limpiar_pantalla(num):
    #Esta funcion lo que hace es solamente limpiar la pantalla de la consola
    time.sleep(num)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    #Funcion que solamente muestra un mensaje por consola
    print("Bienvenido")
    print("Ingrese su contraseña: ")
    menu_requisitos()

def menu_requisitos():
    #Funcion que solamente muestra un mensaje por consola
    print("""
•Tiene que tener una longitud mayor o igual a 8 caracteres
•Tiene que tener al menos una letra en mayúscula y minúscula
•Tiene que tener al menos un número
    """)

def contrasenia():
    #Funcion que pide un ingreso de datos y la guarda en una variable
    contrasenia = input("> ")
    #Retornamos esa variable a uno de los requisitos del ejercicios
    return longitud_contrasenia(contrasenia)

def longitud_contrasenia(contra):
    #Recibe como parametro la contraseña
    #Validamos si la contraseña es mayor o igual a 8 caracteres
    if len(contra) >= 8:
        #Retornamos a otra funcion de validacion
        return letra_mayuscula(contra)
    else:
        #Y si no, retornamos False
        return False

def letra_mayuscula(contra):
    #Recibimos como parametros la contraseña
    #Acá estamos iterando letra por letra sobre la contraseña
    for mayuscula in contra:
        #Y acá vemos si algunas de las letras está en mayuscula comparandola con la lista anteriormente creada
        if mayuscula in LETRAS_ABECEDARIO_MAYUSCULAS:
            #Si todo está bien, retornamos a otra funcion de validacion
            return letra_minuscula(contra)
    else:
        #Y si no, retornamos False
        return False    

def letra_minuscula(contra):
    #Recibimos como parametros la contraseña
    #Acá iteramos letra por letra sobre la contraseña
    for minuscula in contra:
        #Y acá vemos si algunas de las letras está en minuscula comparandola con la lista anteriormente creada
        if minuscula in LETRAS_ABECEDARIO_MINUSCULAS:  
            #Si todo esta bien, retornamos a otra funcion de validacion
            return numeros(contra)
    else:
        #Y si no, retornamos False
        return False

def numeros(contra):
    #Recibimos como parametros la contraseña
    #Iteramos numero por numero sobre la contraseña, que en este caso los numeros serian del tipo str
    for n in contra:
        #Vemos si algún número está en la lista anteriormente creada
        if n in NUMEROS_LISTA:
            #Si todo está bien, retornamos True
            return True
    else:
        #Y si no, retornamos False
        return False

def start():
    #Creamos está funcion para el inicio del programa
    #Creamos un bucle while para iniciar el programa por consola
    while True:
        limpiar_pantalla(1)
        menu()
        #Guardamos el resultado obtenido en una variable, asi poder hacer validaciones
        obtener_resultado = contrasenia()
        #Acá si la variable contiene True, es porque todo esta bien y la contraseña cumple con todos los requisitos
        if obtener_resultado == True:
            print(f"Bien, la contraseña cumple todos los requisitos")
            #Terminamos con el programa
            break
        else:
            #Y si no, es porque la variable contiene el valor bool de False, por lo tanto el programa se reiniciará.
            print(f"La contraseña no pasa todos los requisitos. Vuelve a intentarlo")    

start()



