import uuid

class Producto:
    """Clase que representa un producto de la tienda"""

    def __init__(self, nombre: str, precio: float, stock: int):
        """
        Constructor.

        : param nombre: Nombre del producto
        : param precio: Precio del producto
        : param stock: Cantidad disponible en inventario
        """
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """Retorna el string del producto."""
        return f"Nombre del producto: {self.nombre}\nPrecio: {self.precio}\nStock disponible: {self.stock}"
    
    def actualizar_stock(self, nuevo_stock):
        """Actualiza el stock en inventario."""
        self.stock = nuevo_stock
    
    def suficiente_stock(self, stock_solicitante):
        """Indica si el stock es suficiente."""
        if self.stock >= stock_solicitante:
            return True
        else:
            return False

class ProductoElectronico(Producto):
    """Clase heredada de producto que representa un electrónico de la tienda"""
    def __init__(self, nombre: str, precio: float, stock: int, meses_garantia: int):
        """Constructor
        : param nombre: Nombre del producto
        : param precio: Precio del producto
        : param stock: Cantidad disponible en inventario
        : param meses_garantia: Meses de garantia
        """
        super().__init__(nombre, precio, stock)
        self.meses_garantia = meses_garantia
        
    def __str__(self):
        """Retorna el string del producto."""
        return f"Nombre del producto: {self.nombre}\nPrecio: {self.precio}\nStock disponible: {self.stock}\nMeses de garantía: {self.meses_garantia}"
    
class ProductoRopa(Producto):
    """Clase heredada de producto que representa ropa de la tienda"""
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        """Constructor
        : param nombre: Nombre del producto
        : param precio: Precio del producto
        : param stock: Cantidad disponible en inventario
        : param talla: Talla
        : param color: Color
        """
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color
        
    def __str__(self):
        """Retorna el string del producto."""
        return f"Nombre del producto: {self.nombre}\nPrecio: {self.precio}\nTalla: {self.talla}\nColor: {self.color}\nStock disponible: {self.stock}"
    