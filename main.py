from archivo import cargar_productos, guardar_productos
from inventario import *
from utils import validar_entero, validar_float
from logs import configurar_logger
from colorama import Fore, Style, init

init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + "\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("0. Salir")


def main():
    configurar_logger()
    productos = cargar_productos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                cantidad = validar_entero(input("Cantidad: "))
                precio = validar_float(input("Precio: "))

                agregar_producto(productos, nombre, cantidad, precio)

            elif opcion == "2":
                listar_productos(productos)

            elif opcion == "3":
                id_producto = validar_entero(input("ID: "))
                nueva_cantidad = validar_entero(input("Nueva cantidad: "))
                actualizar_stock(productos, id_producto, nueva_cantidad)

            elif opcion == "4":
                id_producto = validar_entero(input("ID: "))
                eliminar_producto(productos, id_producto)

            elif opcion == "5":
                nombre = input("Nombre: ")
                buscar_producto(productos, nombre)

            elif opcion == "0":
                guardar_productos(productos)
                print(Fore.CYAN + "Saliendo...")
                break

            else:
                print(Fore.RED + "Opción inválida.")

        except ValueError as e:
            print(Fore.RED + f"Error: {e}")


if __name__ == "__main__":
    main()