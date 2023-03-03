"""
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:

Los 3 primeros números corresponden a la patente

El 4 número indica

1- Tiró basura a la vía pública

0 - No tiró basura a la vía pública

El 5 número indica

1- Ya había sido multado el vehículo

0 - Vehículo sin multas.

Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.
"""

" 012 34567"  
# ASD 12345

CANTIDAD_VEHICULOS = 0
VEHICULOS_TIRARON_BASURA = 0
VEHICULOS_MULTADOS = 0
patente = input("Ingresá la patente: ")


while patente.lower() != "fin":
    patente = input("Ingresá la patente: ")
    if len(patente) == 8:
        
        if patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha():
            if patente[3].isdigit() and patente[4].isdigit() and patente[5].isdigit():
                

                if patente[6] == "1" and patente[7] == "1":
                    CANTIDAD_VEHICULOS = CANTIDAD_VEHICULOS + 1
                    VEHICULOS_TIRARON_BASURA = VEHICULOS_TIRARON_BASURA + 1
                    VEHICULOS_MULTADOS = VEHICULOS_MULTADOS + 1
                elif patente[6] == "0" and patente[7] == "0":
                    CANTIDAD_VEHICULOS = CANTIDAD_VEHICULOS+1
                elif patente[6] == "0" and patente[7] == "1":
                    CANTIDAD_VEHICULOS = CANTIDAD_VEHICULOS+1
                    VEHICULOS_MULTADOS = + 1
                elif patente[6] == "1" and patente[7] == "0":
                    CANTIDAD_VEHICULOS = CANTIDAD_VEHICULOS+1
                else:
                    print("Ingresaste mal")
            else:
                print("Hubo un error.")
        else:
            print("Algunas de las primeras 3 letras no cumplen con los requisitos.")
    else:
        print("Pusiste caracteres de más.")
else:
    print(f"""Cantidad de vehiculos: {CANTIDAD_VEHICULOS}.
La cantidad de vehiculos que tiraron basura: {VEHICULOS_TIRARON_BASURA}
La cantidad total de vehiculos multados es: {VEHICULOS_MULTADOS}
""")


