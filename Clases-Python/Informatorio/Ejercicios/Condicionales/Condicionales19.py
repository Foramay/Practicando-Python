"""
Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
"""


salario_obrero = input("¿Cúantas horas trabajaste?: ")


if salario_obrero.isdigit():
    if int(salario_obrero) > 40:
        #Esta variable lo que hace es que a las horas que trabajo del obrero, se le resten 40, asi poder conseguir el resultado de las horas extras
        resultado_hora_extra = int(salario_obrero) - 40
        #Acá multiplico las horas extras
        calculo_horas_extras = int(resultado_hora_extra) * 20
        #Aca hago una multiplicacion para obtener el resultado del pago por las 40 primeras horas
        salario = 40 * 16
        #Y acá sumo el salario de las 40 horas mas el resultado de las horas extas obtenidas
        total_salario = int(salario) + int(calculo_horas_extras)
    elif int(salario_obrero) <= 40: 
        total_salario = int(salario_obrero)* 40 
    print(f"El pago que te corresponde es de ${total_salario}")
else:
    print("Ingresá tu salario nuevamente.")