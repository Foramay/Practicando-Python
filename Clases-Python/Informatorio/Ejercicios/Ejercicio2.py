"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

edad = input("Ingresa tu edad: ")


if edad.isdigit() > 17:
    print(f"Sos mayor de edad. Tu edad es {edad} años.")
elif not edad.isdigit():
    print("Ingresá una edad valida.")
else:
    print(f"Sos menor de edad. Tu edad es {edad} años.")