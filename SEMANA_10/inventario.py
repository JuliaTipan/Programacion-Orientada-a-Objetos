from producto import Producto
import os

class Inventario:
    """
    Clase que representa el sistema de gestión de inventarios de una tienda, con almacenamiento en archivos.
    """

    ARCHIVO = "inventario.txt"  # Nombre del archivo donde se guardará el inventario

    def __init__(self):
        """
        Constructor de la clase Inventario. Inicializa la lista de productos y carga desde el archivo.
        """
        self.productos = []
        self.cargar_desde_archivo()  # Cargar inventario al iniciar

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo inventario.txt.
        Si el archivo no existe, lo crea.
        """
        if not os.path.exists(self.ARCHIVO):
            with open(self.ARCHIVO, "w") as f:
                pass  # Crea el archivo si no existe

        try:
            with open(self.ARCHIVO, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")  # Separar los datos por comas
                    if len(datos) == 4:  # Asegurar que haya 4 valores (id, nombre, cantidad, precio)
                        id_producto, nombre, cantidad, precio = datos
                        producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
        except FileNotFoundError:
            print("El archivo de inventario no existe, creando uno nuevo.")
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
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

    def agregar_producto(self, producto: Producto):
        """
        Agrega un nuevo producto al inventario y lo guarda en el archivo.
        """
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto: int):
        """
        Elimina un producto del inventario y actualiza el archivo.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None):
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

    def buscar_producto(self, nombre: str):
        """
        Busca productos por nombre.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
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

