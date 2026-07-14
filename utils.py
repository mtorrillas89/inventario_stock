def generar_id(productos):
    """
    Genera un ID único para un producto.

    Args:
        productos (list): Lista de productos.

    Returns:
        int: ID generado.
    """
    if not productos:
        return 1
    return max(p["id"] for p in productos) + 1


def validar_entero(valor):
    """
    Valida que el valor sea un número entero.

    Args:
        valor (str): Valor ingresado.

    Returns:
        int: Número entero válido.
    """
    try:
        return int(valor)
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido.")


def validar_float(valor):
    """
    Valida que el valor sea un número decimal.

    Args:
        valor (str): Valor ingresado.

    Returns:
        float: Número decimal válido.
    """
    try:
        return float(valor)
    except ValueError:
        raise ValueError("Debe ingresar un número válido.")