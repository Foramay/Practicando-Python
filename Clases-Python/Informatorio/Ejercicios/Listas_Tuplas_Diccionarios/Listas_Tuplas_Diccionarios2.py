"""
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo contactos hasta que el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.
"""


diccionario = {}

while True:
    nombre = input("Ingresá tu nombre: ")
    gmail = input("Ingresá un gmail: ")
    
    if nombre.isalnum() and gmail.isalnum():
        diccionario.setdefault(nombre, gmail)
    else:
        print("Ingresá algo válido.")


    agregar_mas_contactos = input("¿Querés agregar otro contacto? si/no: ")


    if agregar_mas_contactos.lower() == "no" or agregar_mas_contactos.lower() != "si":
        print("Fin del programa")
        break

print(diccionario)