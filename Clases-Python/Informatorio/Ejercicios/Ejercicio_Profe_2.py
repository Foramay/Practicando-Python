"""
Realizar un programa en Python que valide el nombre de usuario de una persona teniendo en cuenta lo siguiente:
    -Un nombre de usuario es valido, cuando su longitud supere los 8 caracteres
    -No debe incluir los siguientes caracteres especiales: *, -, #, !
    -Tenga al menos 3 vocales
En cada caso, se deberá mostrar un mensaje con el motivo del error.
El programa finaliza cuando el nombre de usuario es valido.
Al finalizar informar:
    -Cantidad de intentos fallidos
"""
CONTADOR_VOCALES = 0
VOCALES = "aeiouAEIOU"
bandera = False
error = 0
print("Bienvenido")

while True:
    nombre_usuario = input("Ingresá el nombre de usuario: ")
    if len(nombre_usuario) > 8:
        if nombre_usuario.isalnum():
            for i in nombre_usuario:
                if i in VOCALES:
                    CONTADOR_VOCALES = CONTADOR_VOCALES + 1
            if CONTADOR_VOCALES < 3:
                error = error + 1 
                print("El nombre de usuario tiene que superar las 3 vocales.")
            else:
                bandera = True
        else:
            error = error + 1 
            print("El nombre de usuaio no debe incluir caracteres especiales.")
        if bandera:
            break
    else:
        error = error + 1 
        print("El nombre de usuario es muy corto")
print(f"""
El usuario '{nombre_usuario}' es válido.
El total de intentos fallidos es de {error}
""")



"""while True:
    nombre_usuario = input("Ingresá el nombre del usuario: ")
    if len(nombre_usuario) > 8 and nombre_usuario.isalnum():
        for i in nombre_usuario:
            if i in VOCALES:
                CONTADOR_VOCALES = CONTADOR_VOCALES + 1
        if CONTADOR_VOCALES < 3:
            print("Tienes que superar las 3 vocales")
        else:
            bandera = True
    else:
        print("Ingresá un nombre de usuario válido.")

    if bandera:
        break
print(f"Nombre de usuario {nombre_usuario} es válido.")"""