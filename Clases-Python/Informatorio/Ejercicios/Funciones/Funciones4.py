"""
Ejercicio 2: Tarifa del taxi

En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado. Escriba un programa principal que use la función.



Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá actualizar fácilmente cuando las tasas aumentan.
"""

TARIFA = 40
TARIFA_ADICIONAL = 15



def obtener_resultado(kilometros):
    for i in range(1, kilometros+1):
        itera = i * 7
        resultado = TARIFA_ADICIONAL * itera
        resultado_final = resultado + TARIFA
    return resultado_final

while True:
    kilometros_recorridos = input("Ingresá los kilometros recorridos: ")
    
    if kilometros_recorridos.isnumeric():
        #formateo_str lo uso para formatear el str a int
        formateo_str = int(kilometros_recorridos)
        #El guardar_resultado lo uso para guardar el resultado obtenido de la funcion obtener_resultado
        guardar_resultado = obtener_resultado(formateo_str)
    else:
        print("Ingresá un valor valido.")
    print(f"El total a pagar es ${guardar_resultado}")   

    