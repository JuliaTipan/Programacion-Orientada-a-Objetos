from producto import Producto

class Inventario:
    """
    Clase que representa el sistema de gestión de inventarios de una tienda.
    """

    def __init__(self):
        """
        Constructor de la clase Inventario. Inicializa una lista vacía de productos.
        """
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """
        Agrega un nuevo producto al inventario, asegurando que el ID sea único.

        :param producto: Instancia de la clase Producto.
        """
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto: int):
        """
        Elimina un producto del inventario por su ID.

        :param id_producto: ID del producto a eliminar.
        """
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.

        :param id_producto: ID del producto a actualizar.
        :param nueva_cantidad: Nueva cantidad en stock (opcional).
        :param nuevo_precio: Nuevo precio del producto (opcional).
        """
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre: str):
        """
        Busca productos por nombre (puede haber coincidencias parciales).

        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos encontrados.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_productos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)


