from services.Tienda_service import TiendaService
from models.Producto import Producto, ProductoElectronico, ProductoRopa

# -------------------- Crear la tienda --------------------
tienda = TiendaService()

# -------------------- Registrar usuarios --------------------
cliente_1 = tienda.registrar_usuario("cliente", "Peman", "peman@example.com", "Calle Mayor 123")
cliente_2 = tienda.registrar_usuario("cliente", "Diego", "diego@example.com", "Avenida Central 45")
cliente_3 = tienda.registrar_usuario("cliente", "Anxo", "anxo@example.com", "Plaza Norte 8")
admin = tienda.registrar_usuario("administrador", "Mario", "mario.admin@example.com")

# -------------------- Crear productos --------------------
producto_1 = ProductoElectronico("Portátil", 1000, 5, 24)
producto_2 = ProductoElectronico("Smartphone", 600, 10, 12)
producto_3 = ProductoRopa("Camiseta", 20, 15, "M", "Rojo")
producto_4 = ProductoRopa("Pantalón", 40, 8, "L", "Azul")
producto_5 = Producto("Libro", 15, 20)

# Añadir productos al inventario
tienda.añadir_producto(producto_1)
tienda.añadir_producto(producto_2)
tienda.añadir_producto(producto_3)
tienda.añadir_producto(producto_4)
tienda.añadir_producto(producto_5)

# -------------------- Listar productos --------------------
print("=== Inventario de la tienda ===")
tienda.listar_productos()

# -------------------- Simular pedidos --------------------
pedido1 = tienda.realizar_pedido(cliente_1.id, [(producto_1, 1), (producto_3, 2)])
pedido2 = tienda.realizar_pedido(cliente_2.id, [(producto_2, 2), (producto_4, 1)])
pedido3 = tienda.realizar_pedido(cliente_3.id, [(producto_5, 3), (producto_3, 1)])

# -------------------- Mostrar histórico de un cliente --------------------
print(f"\n=== Pedidos de {cliente_1.nombre} ===")
tienda.listar_pedidos_por_usuario(cliente_1.id)

# -------------------- Mostrar stock actualizado --------------------
print("\n=== Stock actualizado ===")
tienda.listar_productos()
