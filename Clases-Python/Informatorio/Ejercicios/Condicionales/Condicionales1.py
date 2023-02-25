"""
Los insecticidas se usan para exterminar plagas de insectos. Actúan sobre larvas, huevos o insectos adultos. Uno de los insecticidas más usado fue el DDT, que se caracteriza por ser muy rápido. Trabaja por contacto y es absorbido por la cutícula de los insectos, provocándoles la muerte. 

Este insecticida puede mantenerse por 10 años o más en los suelos y no se descompone.


En nuestro rol de Devs (Programador o Programadora de Software)
- Elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su plantación. 
    - Si hace 10 o más años, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
    - Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".
"""


cantidad_años_uso_insecticida = input("Ingresá hace cuantos años estas usando el insecticida: ")

if cantidad_años_uso_insecticida.isalnum():
    print("Ingesá un número valido por favor.")
elif int(cantidad_años_uso_insecticida) < 10:
    print(f"""
Estás usando el insecticida hace {cantidad_años_uso_insecticida} años.
Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación.""")
else:
    print(f"""
Estás usando el insecticida hace {cantidad_años_uso_insecticida} años.
Por favor solicite revisión de suelos en su plantación.""")