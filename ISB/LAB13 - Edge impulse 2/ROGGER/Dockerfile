# Usa una imagen base de Python
FROM python:3.8-slim

# Instala las bibliotecas necesarias
RUN pip install scipy numpy matplotlib

# Copia el archivo filtrorogger.py al contenedor
COPY filtrorogger.py /usr/src/app/filtrorogger.py

# Define el directorio de trabajo
WORKDIR /usr/src/app

# Comando predeterminado para ejecutar el script
CMD ["python", "filtrorogger.py"]
