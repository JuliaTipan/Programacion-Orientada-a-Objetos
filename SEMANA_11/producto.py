
class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        # Se valida que el ID del producto no sea negativo.
        if id_producto < 0:
            raise ValueError("El ID del producto no puede ser negativo.")

        # Se asegura que la cantidad del producto no sea negativa.
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        # Se verifica que el precio no sea negativo.
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        """
        Metodo para actualizar la cantidad del producto.
        Se asegura que el nuevo valor no sea negativo.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio: float):
        """
        Metodo para actualizar el precio del producto.
        Se verifica que el nuevo precio no sea negativo.
        """
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"