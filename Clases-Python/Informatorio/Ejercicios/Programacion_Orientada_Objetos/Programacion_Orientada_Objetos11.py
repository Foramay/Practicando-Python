"""
Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:


precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9
El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos que comercializa y la suma total de los precios de los mismos.
____________________________________________________________________________________
Suponga ahora que el descuento a aplicar en cada producto de primera necesidad puede ser distinto y se debe poder definir al momento de crear el mismo. Por ejemplo, el arroz puede ser un producto de primera necesidad con un descuento del 8%, mientras que leche podría ser otro producto de primera necesidad con un decuento del 11%. Esto es sólo un ejemplo. El descuento a aplicar en cada producto de primera necesidad debe ser configurable al momento de crearlo.
"""