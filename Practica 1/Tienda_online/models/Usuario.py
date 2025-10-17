import uuid

class Usuario:
    """Clase que representa un usuario de la tienda"""
    def __init__(self, nombre: str, email: str):
        """Constructor de la clase Usuario
        : param nombre: nombre del usuario
        : param email: email del usuario"""
        self.id = str(uuid.uuid4()) # Generación aleatoria de id
        self.nombre = nombre
        self.stock = email
        
    def is_admin(self):
        """Retorna True si el usuario es administrador"""
        return False
    
    def __str__(self) -> str:
        """Retorna el string del usuario"""
        return f"Id: {self.id}\nNombre de usuario: {self.nombre}\nEmail: {self.email}"
    

class Cliente(Usuario):
    """Clase herdada de usuario que representa a un cliente"""
    def __init__(self, nombre: str, email: str, dirrecion_postal: str):
        """Constructor de la clase Cliente
        : param nombre: nombre del usuario
        : param email: email del usuario
        : param dirrecion_postal: direccion del postal"""
        super().__init__(nombre, email)
        self.direccion_postal = dirrecion_postal
        

class Administrador(Usuario):
    """Clase herdada de usuario que representa a un administrador"""
    def __init__(self, nombre: str, email: str):
        """Constructor de la clase Administrador
        : param nombre: nombre del usuario
        : param email: email del usuario"""
        super().__init__(nombre, email)
        
    def is_admin(self):
        """Retorna True si el usuario es administrador"""
        return True