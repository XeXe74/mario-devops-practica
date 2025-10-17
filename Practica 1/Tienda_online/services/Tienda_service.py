from models.Producto import Producto
from models.Usuario import Cliente, Administrador
from models.Pedido import Pedido
from typing import List, Tuple


class TiendaService:
    """Clase que representa a la tienda"""
    def __init__(self):
        """Constructor de la clase tienda"""
        self.usuarios = [] # Se crean listas vacías que contendran los usuarios, productos y pedidos registrados
        self.productos = []
        self.pedidos = []

    # -------------------- USUARIOS --------------------
    def registrar_usuario(self, tipo: str, nombre: str, correo: str, direccion_postal=None):
        """
        Registra un nuevo usuario en la tienda.
        """
        # Si es cliente se comprueba si tiene direccion_postal y se comprueba en general si es cliente o administrador
        if tipo.lower() == "cliente":
            if direccion_postal is None:
                raise ValueError("Se requiere dirección postal para un cliente.")
            usuario = Cliente(nombre, correo, direccion_postal)
        elif tipo.lower() == "administrador":
            usuario = Administrador(nombre, correo)
        else:
            raise ValueError("Tipo de usuario no válido. Debe ser 'cliente' o 'administrador'.")

        self.usuarios.append(usuario)
        return usuario

    # -------------------- PRODUCTOS --------------------
    def añadir_producto(self, producto: Producto):
        """
        Añade un producto al inventario de la tienda.
        """
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de Producto o sus subclases.")
        self.productos.append(producto)
        return producto

    def eliminar_producto(self, producto_id: str):
        """
        Elimina un producto del inventario por su ID.
        """
        # Se recorre la lista de productos para eliminar el producto
        for prod in self.productos:
            if prod.id == producto_id:
                self.productos.remove(prod)
                return True
        return False

    def listar_productos(self):

        # Se listan todos los productos
        for prod in self.productos:
            print(prod)
            print("---")

    # -------------------- PEDIDOS --------------------
    def realizar_pedido(self, usuario_id: str, lista_productos: List[Tuple[Producto, int]]):
        """ Realiza un pedido de un usuario en la tienda."""
        # Buscar usuario por id
        usuario = None
        for u in self.usuarios:
            if u.id == usuario_id:
                usuario = u
                break

        if usuario is None:
            raise ValueError("Usuario no encontrado.")

        if not isinstance(usuario, Cliente):
            raise ValueError("Solo los clientes pueden realizar pedidos.")
            
        for producto, cantidad in lista_productos:
            if not producto.suficiente_stock(cantidad):
                raise ValueError(f"No hay suficiente stock de {producto.nombre}.")

        # Descontar stock
        for producto, cantidad in lista_productos:
            producto.actualizar_stock(producto.stock - cantidad)

        # Crear pedido
        pedido = Pedido(usuario, lista_productos)
        self.pedidos.append(pedido)

        return pedido

    def listar_pedidos_por_usuario(self, usuario_id: str):
        """ Lista los pedidos realizados por un usuario en la tienda, ordenados por fecha"""
        pedidos_usuario = []

        # Filtrar pedidos del usuario
        for pedido in self.pedidos:
            if pedido.cliente.id == usuario_id:
                pedidos_usuario.append(pedido)

        # Comprobar si existe el usuario
        if not pedidos_usuario:
            print("El usuario no tiene pedidos.")
            return

        # Ordenar por fecha
        pedidos_usuario = sorted(pedidos_usuario, key=lambda p: p.fecha)

        # Imprimir cada pedido
        for ped in pedidos_usuario:
            print(ped)
            print("---")  # Separador entre pedidos
