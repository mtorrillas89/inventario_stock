from utils import generar_id
from logs import registrar_log
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)


def agregar_producto(productos, nombre, cantidad, precio):
    """
    Agrega un producto al inventario.
    """
    producto = {
        "id": generar_id(productos),
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    productos.append(producto)
    registrar_log(Fore.GREEN + f"Producto agregado: {nombre}")


def listar_productos(productos):
    """
    Lista todos los productos en formato tabla.
    """
    if not productos:
        print(Fore.RED + "No hay productos.")
        return

    tabla = [[p["id"], p["nombre"], p["cantidad"], p["precio"]] for p in productos]
    print(tabulate(tabla, headers=["ID", "Nombre", "Cantidad", "Precio"], tablefmt="grid"))


def actualizar_stock(productos, id_producto, nueva_cantidad):
    """
    Actualiza el stock de un producto.
    """
    for p in productos:
        if p["id"] == id_producto:
            p["cantidad"] = nueva_cantidad
            registrar_log(f"Stock actualizado: {p['nombre']}")
            return

    print("Producto no encontrado.")


def eliminar_producto(productos, id_producto):
    """
    Elimina un producto.
    """
    for p in productos:
        if p["id"] == id_producto:
            productos.remove(p)
            registrar_log(f"Producto eliminado: {p['nombre']}")
            print(Fore.GREEN + f"Producto '{p['nombre']}' eliminado correctamente.")
            return

    print(Fore.RED + "Producto no encontrado.")

def buscar_producto(productos, nombre):
    """
    Busca productos por nombre.
    """
    resultados = [p for p in productos if nombre.lower() in p["nombre"].lower()]

    if not resultados:
        print("No se encontraron productos.")
        return

    tabla = [[p["id"], p["nombre"], p["cantidad"], p["precio"]] for p in resultados]
    print(tabulate(tabla, headers=["ID", "Nombre", "Cantidad", "Precio"], tablefmt="grid"))