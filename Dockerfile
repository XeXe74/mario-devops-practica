# Usar la imagen base especificada
FROM python:3.12-slim

# Metadata
LABEL authors="mariotg"
LABEL description="Tienda Service - Práctica 1.3"

# Establecer directorio de trabajo
WORKDIR /app

# Copiar primero solo requirements.txt para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la estructura del proyecto
COPY ["Practica 1/", "./Practica 1/"]

# Crear un usuario no privilegiado para mayor seguridad
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Cambiar al usuario no privilegiado
USER appuser

# Comando de inicio - ejecutar el main.py principal
CMD ["python", "Practica 1/Tienda_online/main.py"]


