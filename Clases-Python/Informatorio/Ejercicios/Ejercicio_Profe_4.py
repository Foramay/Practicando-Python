"""
Ejercicio 3:
Escribir un programa en python que solicite el ingreso de las clasificaciones y el nombre y apellido de un numero dado de alumnos (este número lo establece inicialmente el operador)
    Consideraciones:
        -El nombre y apellido se ingresan en una sola instruccion con el siguiente formato: Nombres APELLIDOS (es decir, un alumno puede tener varios nombres, pero un solo apellido, cada uno se lo separara por un espacio)
    Al finalizar informar:
        -Cantidad de alumnos aprobados (nota >= 6)
        -Cantidad de alumnos desaprobados (nota <6)
        -Nombre y calificacion del alumno con la nota mas baja.
        -Cantidad de alumnos cuyo nombre sea Juan

"""
APROBADOS = 0
DESAPROBADOS = 0
JUANCITOS = 0
NOTA_BAJA = 11
NOMBRE_NOTA_BAJA = ""
cantidad_alumnos = input("Ingresá la cantidad de alumnos: ")


for i in range(int(cantidad_alumnos)):
    nombre_apellido_alumno = input(f"Ingresá el nombre y apellido del alumno {i+1}: ").title()
    calificacion = input(f"Ingresá la calificacion de {nombre_apellido_alumno}: ")

    if int(calificacion) < 6:
        DESAPROBADOS = DESAPROBADOS + 1
    elif int(calificacion) >= 6:
        APROBADOS = APROBADOS + 1

    if nombre_apellido_alumno.split(" ")[0] == "Juan" or nombre_apellido_alumno.split(" ")[1] == "Juan":
        JUANCITOS = JUANCITOS + 1

    if int(calificacion) < int(NOTA_BAJA):
        NOTA_BAJA = calificacion
        NOMBRE_NOTA_BAJA = nombre_apellido_alumno
print(f"""
La cantidad de alumnos aprobados es de {APROBADOS}.
La cantidad de alumnos desaprobados es de {DESAPROBADOS}.
El alumno con la nota más baja es {NOMBRE_NOTA_BAJA} con {NOTA_BAJA}.
La cantidad de Juancitos es de {JUANCITOS}.
""")