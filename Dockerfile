# Usa la imagen base de Python
FROM python:3.10.12

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de requerimientos
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación
COPY . .

# Expón el puerto en el que tu aplicación Django se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
