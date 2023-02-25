"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
    -Escribir un programa que pregunte al usuario su nombre y sexo
    -Mostrar por pantalla el grupo que le corresponde.
"""

nombre = input("¿Cúal es tu nombre?: ")
sexo = input("¿Cúal es tu genero): ")

#Forma 1

"""if nombre.lower() < "m" and sexo.lower() == "femenino":
    print(f"Perteneces al grupo A {nombre.capitalize()}")
elif nombre.lower() > "n" and sexo.lower() == "masculino":
    print(f"Perteneces al grupo A {nombre.capitalize()}")
else:
    print(f"Perteneces al grupo B {nombre.capitalize()}")"""

#Forma 2

if (nombre.lower() < "m" and sexo.lower() == "femenino") or (nombre.lower() > "n" and sexo.lower() == "masculino"):
    print(f"Perteneces al grupo A {nombre.capitalize()}")
else:
    print(f"Perteneces al grupo B {nombre.capitalize()}")