import tkinter as tk
from tkinter import messagebox, ttk

from archivo import cargar_productos, guardar_productos
from inventario import agregar_producto, actualizar_stock, eliminar_producto

productos = cargar_productos()

orden_asc = True  # para ordenar columnas


# ---------------- FUNCIONES ---------------- #

def refrescar_tabla(lista=None):
    """Carga productos en la tabla."""
    for fila in tabla.get_children():
        tabla.delete(fila)

    datos = lista if lista else productos

    for p in datos:
        tabla.insert("", "end", values=(p["id"], p["nombre"], p["cantidad"], p["precio"]))


def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)


def agregar():
    try:
        nombre = entry_nombre.get()
        cantidad = int(entry_cantidad.get())
        precio = float(entry_precio.get())

        agregar_producto(productos, nombre, cantidad, precio)
        guardar_productos(productos)

        refrescar_tabla()
        limpiar_campos()
        messagebox.showinfo("OK", "Producto agregado")

    except ValueError:
        messagebox.showerror("Error", "Datos inválidos")


def seleccionar_fila(event):
    seleccionado = tabla.focus()
    if seleccionado:
        valores = tabla.item(seleccionado, "values")

        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])

        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(0, valores[2])

        entry_precio.delete(0, tk.END)
        entry_precio.insert(0, valores[3])


def actualizar():
    try:
        seleccionado = tabla.focus()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto")
            return

        valores = tabla.item(seleccionado, "values")
        id_producto = int(valores[0])
        nueva_cantidad = int(entry_cantidad.get())

        actualizar_stock(productos, id_producto, nueva_cantidad)
        guardar_productos(productos)

        refrescar_tabla()
        messagebox.showinfo("OK", "Stock actualizado")

    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida")


def eliminar():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Atención", "Seleccione un producto")
        return

    valores = tabla.item(seleccionado, "values")
    id_producto = int(valores[0])

    if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
        eliminar_producto(productos, id_producto)
        guardar_productos(productos)

        refrescar_tabla()
        limpiar_campos()


# ---------------- BUSQUEDA ---------------- #

def buscar():
    texto = entry_buscar.get().lower()
    filtrados = [p for p in productos if texto in p["nombre"].lower()]
    refrescar_tabla(filtrados)


# ---------------- FILTROS ---------------- #

def filtrar_precio():
    try:
        precio_min = float(entry_precio_min.get())
        filtrados = [p for p in productos if p["precio"] >= precio_min]
        refrescar_tabla(filtrados)
    except ValueError:
        messagebox.showerror("Error", "Precio inválido")


def filtrar_stock_bajo():
    filtrados = [p for p in productos if p["cantidad"] < 5]
    refrescar_tabla(filtrados)


def mostrar_todos():
    refrescar_tabla()


# ---------------- ORDENAMIENTO ---------------- #

def ordenar_columna(col):
    global orden_asc

    datos = [(tabla.set(k, col), k) for k in tabla.get_children()]

    try:
        datos.sort(key=lambda x: float(x[0]), reverse=not orden_asc)
    except:
        datos.sort(reverse=not orden_asc)

    for index, (val, k) in enumerate(datos):
        tabla.move(k, "", index)

    orden_asc = not orden_asc


# ---------------- INTERFAZ ---------------- #

ventana = tk.Tk()
ventana.title("Sistema de Inventario PRO")
ventana.geometry("750x500")

# ---------------- INPUTS ---------------- #

frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_inputs)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_inputs, text="Cantidad").grid(row=1, column=0)
entry_cantidad = tk.Entry(frame_inputs)
entry_cantidad.grid(row=1, column=1)

tk.Label(frame_inputs, text="Precio").grid(row=2, column=0)
entry_precio = tk.Entry(frame_inputs)
entry_precio.grid(row=2, column=1)

# ---------------- BOTONES ---------------- #

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Agregar", width=12, command=agregar).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Actualizar", width=12, command=actualizar).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar", width=12, command=eliminar).grid(row=0, column=2, padx=5)

# ---------------- BUSQUEDA ---------------- #

frame_busqueda = tk.Frame(ventana)
frame_busqueda.pack(pady=5)

tk.Label(frame_busqueda, text="Buscar").pack(side="left")
entry_buscar = tk.Entry(frame_busqueda)
entry_buscar.pack(side="left", padx=5)

tk.Button(frame_busqueda, text="Buscar", command=buscar).pack(side="left")
tk.Button(frame_busqueda, text="Mostrar todo", command=mostrar_todos).pack(side="left")

entry_buscar.bind("<KeyRelease>", lambda e: buscar())

# ---------------- FILTROS ---------------- #

frame_filtros = tk.Frame(ventana)
frame_filtros.pack(pady=5)

tk.Label(frame_filtros, text="Precio mínimo").pack(side="left")
entry_precio_min = tk.Entry(frame_filtros, width=10)
entry_precio_min.pack(side="left", padx=5)

tk.Button(frame_filtros, text="Filtrar Precio", command=filtrar_precio).pack(side="left", padx=5)
tk.Button(frame_filtros, text="Stock Bajo (<5)", command=filtrar_stock_bajo).pack(side="left", padx=5)

# ---------------- TABLA ---------------- #

tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")

for col in ("ID", "Nombre", "Cantidad", "Precio"):
    tabla.heading(col, text=col, command=lambda c=col: ordenar_columna(c))

tabla.pack(fill="both", expand=True)

tabla.bind("<<TreeviewSelect>>", seleccionar_fila)

# ---------------- INIT ---------------- #

refrescar_tabla()

ventana.mainloop()