import json
import os

RUTA_ARCHIVO = "data/productos.json"


def cargar_productos():
    """
    Carga los productos desde un archivo JSON.

    Returns:
        list: Lista de productos.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "w") as archivo:
            json.dump([], archivo)

    try:
        with open(RUTA_ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def guardar_productos(productos):
    """
    Guarda los productos en un archivo JSON.

    Args:
        productos (list): Lista de productos.
    """
    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(productos, archivo, indent=4)