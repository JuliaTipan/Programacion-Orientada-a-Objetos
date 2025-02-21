from inventario import Inventario
from producto import Producto


def menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar inventario")
    print("5. Buscar producto")
    print("6. Salir")


inventario = Inventario()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_producto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio = float(input("Ingrese el precio del producto: "))

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        inventario.agregar_producto(nuevo_producto)

    elif opcion == "2":
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad (o presione Enter para no cambiar): ") or -1)
        nuevo_precio = float(input("Ingrese el nuevo precio (o presione Enter para no cambiar): ") or -1)

        inventario.actualizar_producto(id_producto,
                                       nueva_cantidad if nueva_cantidad != -1 else None,
                                       nuevo_precio if nuevo_precio != -1 else None)

    elif opcion == "4":
        inventario.mostrar_productos()

    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        productos_encontrados = inventario.buscar_producto(nombre)
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print("No se encontraron productos.")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")