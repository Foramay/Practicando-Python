"""
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

    - Escribir un programa que pregunte al usuario que tipo de receta desea
    - En función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
    - Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta.
    - Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
"""
#Creo una lista vacia para despúes agregar valores a ella.
ingredientes_elegidos = []

print("""
Bienvenido
1 - Receta 1
    - Lentejas y apio
2 - Receta 2
    - Morrón y Cebolla
""")
receta_usuario = input("¿Qué tipo de receta desea?: ")

if not receta_usuario.isdigit():
    print("Elegí una opcion usando los números.")
elif int(receta_usuario) == 1:
    for i in range(3):
        print("""
        Elegí tus ingredientes
            1 - Verduras
            2 - Berenjenas
            3 - Lenteja
            4 - Apío
        """)
        ingredientes_usuario = input("> ")
        if not ingredientes_usuario.isdigit():
            break
        elif int(ingredientes_usuario) == 1:
            ingredientes_elegidos.append("Verduras")
        elif int(ingredientes_usuario) == 2:
            ingredientes_elegidos.append("Berenjenas")
        elif int(ingredientes_usuario) == 3:
            ingredientes_elegidos.append("Lenteja")
        elif int(ingredientes_usuario) == 4:
            ingredientes_elegidos.append("Apío")
        else:
            print("No existe esa opcion")
    tipo_receta = "la 1, que contiene Lentejas y Apio."
elif int(receta_usuario) == 2:
    for i in range(3):
        print("""
        Elegí tus ingredientes
            1 - Verduras
            2 - Berenjenas
            3 - Morrón
            4 - Cebolla
        """)
        ingredientes_usuario = input("> ")
        if not ingredientes_usuario.isdigit():
            break
        elif int(ingredientes_usuario) == 1:
            ingredientes_elegidos.append("Verduras")
        elif int(ingredientes_usuario) == 2:
            ingredientes_elegidos.append("Berenjenas")
        elif int(ingredientes_usuario) == 3:
            ingredientes_elegidos.append("Morrón")
        elif int(ingredientes_usuario) == 4:
            ingredientes_elegidos.append("Cebolla")
        else:
            print("No existe esa opcion")
    tipo_receta = "la 1, que contiene Morrón y Cebolla."
print(f"""La receta elegida es la {tipo_receta}.
Los ingredientes que elegiste fueron {ingredientes_elegidos}
""")