# 📦 Sistema de Gestión de Inventario en Python

## 📌 Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python, ejecutado desde consola (CLI). Permite administrar productos mediante operaciones básicas como alta, modificación, eliminación y consulta.

El objetivo del proyecto es aplicar buenas prácticas de programación, incluyendo modularización, documentación con docstrings, manejo de errores y uso de herramientas profesionales como Git y entornos virtuales.

---

## ⚙️ Funcionalidades

* Agregar productos al inventario
* Listar productos en formato tabla
* Actualizar stock
* Eliminar productos
* Buscar productos por nombre
* Persistencia de datos en archivo JSON
* Registro de eventos mediante logging
* Validación de datos de entrada

---

## 🧩 Estructura del proyecto

```
inventario/
│
├── main.py
├── inventario.py
├── archivo.py
├── utils.py
├── logs.py
│
├── data/
│   └── productos.json
│
├── logs/
│   └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧠 Tecnologías utilizadas

* Python 3
* JSON (persistencia de datos)
* Logging (registro de eventos)
* Tabulate (visualización en tabla)
* Colorama (opcional, mejora visual en consola)

---

## 🚀 Ejecución del programa

1. Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Crear entorno virtual:

```
python -m venv venv
```

3. Activar entorno virtual:

* Windows:

```
venv\Scripts\activate
```

4. Instalar dependencias:

```
pip install -r requirements.txt
```

5. Ejecutar el programa:

```
python main.py
```

---

## 📄 Ejemplo de uso

El sistema muestra un menú interactivo donde el usuario puede seleccionar diferentes opciones para gestionar el inventario.

---

## 🧪 Manejo de errores

Se implementa manejo de errores utilizando bloques try/except para validar entradas del usuario, evitando fallos en la ejecución del programa.

---

## 📚 Buenas prácticas aplicadas

* Código modularizado
* Uso de funciones
* Docstrings según PEP 257
* Estilo de código según PEP 8
* Separación de responsabilidades
* Uso de entorno virtual

---

## 🤖 Uso de Inteligencia Artificial

Durante el desarrollo se utilizó inteligencia artificial como apoyo para:

* Comprender conceptos
* Mejorar la estructura del código
* Redactar documentación

El código fue revisado, comprendido y adaptado manualmente para asegurar su correcto funcionamiento.

---

## 📌 Conclusión

Este proyecto representa una implementación básica pero sólida de un sistema de inventario, aplicando conceptos fundamentales de programación y buenas prácticas profesionales.

---
