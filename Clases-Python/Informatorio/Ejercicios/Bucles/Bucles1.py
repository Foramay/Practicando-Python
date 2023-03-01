"""
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 
"""


#Desafío forma 1
CONTRASEÑA = "asd"
contraseña = input("Ingresá la contraseña: ")
while contraseña != CONTRASEÑA:
        print("Contraseña incorrecta. Volvé a escribir")
        contraseña = input("Ingresá la contraseña: ")        
print("Contraseña correcta.")


#Desafío forma 2
"""
for i in range(3):
    contraseña = input("Ingresá tu contraseña: ")
    if contraseña != CONTRASEÑA:
        print("Contraseña incorecta.")
    else:
        print("Contraseña correcta.")
        break
"""