import os
from producto import Producto


class Inventario:
    """
    Clase que representa el sistema de gestión de inventarios de una tienda, con almacenamiento en archivos.
    """

    ARCHIVO = "inventario.txt"  # Nombre del archivo donde se guardará el inventario

    def __init__(self):
        """
        Constructor de la clase Inventario. Inicializa la lista de productos y carga desde el archivo.
        """
        self.productos = []  # Lista para almacenar productos
        self.cargar_desde_archivo()  # Cargar inventario al iniciar

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo inventario.txt.
        Si el archivo no existe, lo crea.
        """
        if not os.path.exists(self.ARCHIVO):
            open(self.ARCHIVO, "w").close()  # Crea el archivo si no existe

        try:
            with open(self.ARCHIVO, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")  # Separar los datos por comas
                    if len(datos) == 4:  # Asegurar que haya 4 valores (id, nombre, cantidad, precio)
                        id_producto, nombre, cantidad, precio = datos
                        self.productos.append(Producto(int(id_producto), nombre, int(cantidad), float(precio)))
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo inventario.txt.
        """
        try:
            with open(self.ARCHIVO, "w") as f:
                for producto in self.productos:
                    f.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario y lo guarda en el archivo.
        """
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario y actualiza el archivo.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto y lo guarda en el archivo.
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("Producto no encontrado.")

    def mostrar_productos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)


if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = int(input("ID del producto: "))
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")