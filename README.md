# Mario DevOps - Práctica 2.2

Proyecto de contenerización de una aplicación Python de gestión de tienda online desarrollada en la Práctica 1.3.

## Descripción

Este proyecto implementa un sistema de gestión de tienda online con las siguientes clases:
- **Usuario**: Gestión de clientes
- **Producto**: Catálogo de productos
- **Pedido**: Procesamiento de pedidos
- **TiendaService**: Servicio principal que coordina las operaciones

## Estructura del Proyecto

Programas/
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── Practica 1/
└── Tienda_onl
ne/
├── main.py
init.py
│ ├── Us
ario.py │
├── Producto.py
│ └──
init.py
└── T


## Requisitos Previos

- Docker Desktop instalado y en ejecución
- Git configurado
- Python 3.12 (solo para desarrollo local)

## Docker

### Cómo construir la imagen

docker build -t mario-tienda:latest .


Este comando:
- Lee el Dockerfile en el directorio actual
- Construye una imagen basada en python:3.12-slim
- Instala todas las dependencias de requirements.txt
- Copia el código fuente al contenedor
- Etiqueta la imagen como mario-tienda:latest

### Cómo ejecutar la imagen

**Ejecución básica:**
docker run --rm --name tienda-app mario-tienda:latest


### Parámetros de docker run

- `--rm`: Elimina el contenedor automáticamente cuando termina la ejecución
- `--name`: Asigna un nombre específico al contenedor
- `-it`: Modo interactivo con terminal
- `/bin/bash`: Abre una shell en lugar de ejecutar la aplicación

### Variables de entorno soportadas

Actualmente la aplicación no requiere variables de entorno externas. Todas las configuraciones están incluidas en el código.

### Salida esperada

Al ejecutar el contenedor, deberías ver la siguiente salida:

=== Inventario de la tienda ===
Nombre del producto: Portátil
Precio: 1000
Stock disponible: 5
Meses de garantía: 24
---
Nombre del producto: Smartphone
Precio: 600
Stock disponible: 10
Meses de garantía: 12
---
Nombre del producto: Camiseta
Precio: 20
Talla: M
Color: Rojo
Stock disponible: 15
---
Nombre del producto: Pantalón
Precio: 40
Talla: L
Color: Azul
Stock disponible: 8
---
Nombre del producto: Libro
Precio: 15
Stock disponible: 20
---

=== Pedidos de Peman ===
ID: 98256550-c0ed-486f-ad19-a4c3be4ed667
Fecha: 2025-11-21 15:35:30
Cliente: Peman
Productos:
  - Portátil x 1 = 1000.00 €
  - Camiseta x 2 = 40.00 €

TOTAL: 1040.00 €
---

=== Stock actualizado ===
Nombre del producto: Portátil
Precio: 1000
Stock disponible: 4
Meses de garantía: 24
---
Nombre del producto: Smartphone
Precio: 600
Stock disponible: 8
Meses de garantía: 12
---
Nombre del producto: Camiseta
Precio: 20
Talla: M
Color: Rojo
Stock disponible: 12
---
Nombre del producto: Pantalón
Precio: 40
Talla: L
Color: Azul
Stock disponible: 7
---
Nombre del producto: Libro
Precio: 15
Stock disponible: 17
---