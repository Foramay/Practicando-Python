"""Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)         Aumento

0 – 6000					  15%

6000 – 7900					  10%

7900 – 12000				   6%

Más de 12000				   0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado."""

sueldoJugador = int(input("Ingresá tu sueldo actual: $"))


if sueldoJugador < 6000:
    sueldoJugador
    print(f"""Te corresponde el %15 de aumento.
Tu sueldo actual es de ---- ${sueldoJugador}.
Ahora tu sueldo será de ---- ${sueldoJugador*15}
    """)
elif sueldoJugador >= 6000 and sueldoJugador < 7900:
    print(f"""Te corresponde el %10 de aumento.
Tu sueldo actual es de ---- ${sueldoJugador}.
Ahora tu sueldo será de ---- ${sueldoJugador*10}
    """)
elif sueldoJugador >= 7900 and sueldoJugador < 12000:
    print(f"""Te corresponde el %6 de aumento.
Tu sueldo actual es de ---- ${sueldoJugador}.
Ahora tu sueldo será de ---- ${sueldoJugador*6}
    """)
else:
    print("Tu sueldo es superior a $12000, no mereces aumentos caradura.")