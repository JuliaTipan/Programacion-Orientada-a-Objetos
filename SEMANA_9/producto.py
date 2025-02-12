class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.

        :param id_producto: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad en stock.
        :param precio: Precio unitario.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
