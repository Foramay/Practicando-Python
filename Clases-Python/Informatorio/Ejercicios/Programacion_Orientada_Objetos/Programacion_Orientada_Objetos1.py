"""
Desarrollar un programa que cargue los datos de un triángulo.

Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""

TRIANGULO = []
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def longitud_maxima(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if (self.lado1 == self.lado2 and self.lado1 != self.lado3) or (self.lado2 == self.lado3 and self.lado3 != self.lado1) or (self.lado1 == self.lado3 and self.lado1 != self.lado2):
            return f'isósceles'
        elif self.lado1 != self.lado2 and self.lado2 != self.lado3:
            return f'escaleno'
        else:
            return f'equilatero'
triangulo_lado1 = input("Ingresá el lado 1: ")
triangulo_lado2 = input("Ingresá el lado 2: ")
triangulo_lado3 = input("Ingresá el lado 3: ")


triangulo = Triangulo(lado1=triangulo_lado1, lado2=triangulo_lado2, lado3=triangulo_lado3)
print(f'El tipo de triangulo es {triangulo.tipo_triangulo()}\nEl lado mayor es {triangulo.longitud_maxima()}')