import datetime, uuid
from models.Usuario import Cliente
from models.Producto import Producto
from typing import List, Tuple

class Pedido:
    """Representa un pedido de un cliente con productos y cantidades."""

    def __init__(self, cliente: Cliente, productos: List[Tuple[Producto, int]]): # Constructor
        """
        Constructor del pedido.

        : param cliente: Cliente que realiza el pedido
        : param productos: Lista de tuplas (Producto, cantidad)
        """
        self.id = str(uuid.uuid4()) # Generación de número aleatorio
        self.fecha = datetime.datetime.now()
        self.cliente = cliente
        self.productos = productos  # lista
        
    def calcular_total(self):
        """Calcula el importe total del pedido."""
        return sum(prod.precio * cant for prod, cant in self.productos)
        
    def __str__(self):
        """ Retorna el string del pedido."""
        
        productos_str = ""
        
        for prod, cant in self.productos: # Se crea un string con todos los productos y sus precios
            productos_str += f"  - {prod.nombre} x {cant} = {prod.precio * cant:.2f} €\n"
            
        return (f"ID: {self.id}\n"
                f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Productos:\n{productos_str}\n"
                f"TOTAL: {self.calcular_total():.2f} €")