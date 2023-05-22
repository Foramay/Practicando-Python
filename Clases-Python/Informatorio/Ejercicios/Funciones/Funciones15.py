import string, random
"""
Ejercicio 13: Contraseña aleatoria

-Escriba una función que genere una contraseña aleatoria. 
-La contraseña debe tener una longitud aleatoria de entre 7 y 10 caracteres. 
-Cada carácter debe seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII. Su función no tomará ningún parámetro y devolverá la contraseña generada aleatoriamente como su único resultado. Desarrolle un programa principal y muestre la contraseña generada aleatoriamente.



Sugerencia: Probablemente encuentre útil la función chr cuando complete este ejercicio.
"""


def random_number():
    #Esta función me devuelve un numero aleatorio para la longitud de la contraseña
    numero_random = random.randint(7, 10)
    return random_password(numero_random)

def random_password(number):
    #Esta funcion me retorna la contraseña aleatoria, recibe como parámetro un numero aleatorio de la función random_number()
    #Creo una variable para almacenar las letras aleatorias que me da la funcion random.choice
    password_random = ""
    #Lo que hago es iterar la cantidad de veces con el numero aleatorio que recibo como parámetro
    for password in range(1, number+1):
        #Hago que me de una letra aleatoria
        letra_contrasenia = random.choice(string.ascii_letters)
        #Y la guardo en la variable
        password_random += letra_contrasenia 
    #Al final del for, retorno la contraseña
    return password_random


print(f"La contraseña aleatoria es: {random_number()}")