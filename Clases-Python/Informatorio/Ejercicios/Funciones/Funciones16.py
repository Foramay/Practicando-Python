import string, random
"""
Ejercicio 14: Matricula aleatoria

En una jurisdicción particular, las matrículas más antiguas consisten en tres letras seguidas de tres números. Cuando se utilizaron todas las placas que siguen ese patrón, el formato se cambió a cuatro números seguidos de tres letras. 
-Escriba una función que genere una matrícula aleatoria. 
-Escriba un programa principal que llame a su función y muestre la placa generada al azar.
"""

def random_letras():
    #Esta funcion crea letras al azar para la matricula
    placa_letras = ""
    for l in range(1, 4):
        #Acá lo que hace es elegir una letra al azar 
        letra_aleatoria = random.choice(string.ascii_letters)
        #Y acá la guarda en una variable
        placa_letras += letra_aleatoria
    #Y retorno la variable
    return placa_letras

def random_numeros():
    #Esta funcio crea numeros al azar para la matricula
    placa_numeros = ""
    for n in range(1, 4):
        #Acá me elige un numero al azar del 0 al 9
        numero_aleatorio = random.randint(0, 9)
        #Acá parseo el numero del tipo int a str para asi poder concatenar con la variable de la funcion random_letras()
        parseo_a_str = str(numero_aleatorio)
        #Acá lo guardo en una variable
        placa_numeros += parseo_a_str
    #Y retorno la variable
    return placa_numeros

def placa_final():
    #Aca recibo lo que retorna las variables y lo guardo en una nueva
    placa_letras = random_letras()
    placa_numeros = random_numeros()
    #Para asi poder mostrar por consola
    print(f"La placa aleatoria es: {placa_letras} {placa_numeros}")

def start():
    placa_final()

print("Bienvenido.")
start()
