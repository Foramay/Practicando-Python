"""
Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.
"""

calificacion1 = input("Ingresá la primer nota: ")
calificacion2 = input("Ingresá la segunda nota: ")
calificacion3 = input("Ingresá la tercer nota: ") 


if calificacion1.isdigit() and calificacion2.isdigit() and calificacion3.isdigit():
    promedio = int(calificacion1) + int(calificacion2) + int(calificacion3) // 3
    if int(promedio) >= 7:
        print(f"Estás aprobado. El resultado de tus calificaciones es de {promedio}")
    else:
        print("Estás desaprobado.")
else:
    print("Por favor ingresá la nota.") 


