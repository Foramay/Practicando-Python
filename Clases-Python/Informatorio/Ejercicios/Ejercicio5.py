"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
-Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
- Mostrar por pantalla si el usuario tiene que tributar o no.
"""


edad = int(input("Ingresá tu edad: "))
ingresos = int(input("Ingresá tus ingresos: $"))

if edad > 16 and ingresos >= 1000:
    print("Podes tribuar.")
elif edad < 16 or ingresos < 1000:
    print("No podes tributar")
else:
    print("No podes tributar.")