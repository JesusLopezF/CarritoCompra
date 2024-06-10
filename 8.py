"""
8. Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito,
se compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo elemento.
Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito.
En esta nueva versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega.
El contenido del programa principal es idéntico al ejercicio anterior.

Salida:

Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Hay 2 productos en la cesta.
El total asciende a 488,90 euros
Continúa la compra...
Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 3 Subtotal: 59,85
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Ahora hay 3 productos en la cesta.
El total asciende a 1105,85 euros
"""

from typeguard import typechecked


@typechecked
class Elemento:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} PVP: {self.precio:.2f} Unidades: {self.cantidad} Subtotal: {self.precio * self.cantidad:.2f}"


@typechecked
class Carrito:
    def __init__(self):
        self.elementos = []

    def agrega(self, elemento: 'Elemento'):
        if elemento in self.elementos:
            elemento.cantidad += 1
        else:
            self.elementos.append(elemento)

    def __str__(self):
        return "\n".join(str(elemento) for elemento in self.elementos)

    def numero_elementos(self):
        return len(self.elementos)

    def importe_total(self):
        return sum(elemento.precio * elemento.cantidad for elemento in self.elementos)


mi_carrito = Carrito()
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.numero_elementos()} productos en la cesta.")
