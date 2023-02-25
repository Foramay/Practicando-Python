"""
En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		        PORCENTAJE

Pediatría			60%

Traumatología		20%

Kinesiología		20%


Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 		que se ingrese por teclado.
"""

presupuesto_anual = input("Ingresá el presupuesto anual: $")

if presupuesto_anual.isdigit():
    total_pedriatria = 60 * int(presupuesto_anual) // 100
    total_traumatologia = 20 * int(presupuesto_anual) // 100
    total_kinesiologia = 20 * int(presupuesto_anual) // 100    
    print(f"""
El monto total por año es de === ${presupuesto_anual}
El monto que recibirá el área de Pedriatría es de === ${float(total_pedriatria)}
El monto que recibirá el área de Traumatología es de === ${float(total_traumatologia)}
El monto que recibirá el área de Kinesiología es de === ${float(total_kinesiologia)}
    """)
else:
    print("No")