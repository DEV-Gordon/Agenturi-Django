# Agenturi-Django

Proyecto desarrollado con Django y ejecutado en WSL (Ubuntu).
Este repositorio contiene la aplicación principal y los archivos necesarios para ejecutar el proyecto en entorno local.

## Requisitos previos

Asegúrate de tener instalado en tu entorno WSL (Ubuntu) lo siguiente:

```
sudo apt update
sudo apt install python3 python3-venv python3-pip git -y
```

También puedes abrir el proyecto fácilmente con Visual Studio Code:

```
code .
```

## Clonar el repositorio

Ejecuta los siguientes comandos en tu terminal WSL:

### 1. Ir al directorio donde guardarás el proyecto
```
cd ~/
```

### 2. Clonar el repositorio
```
git clone https://github.com/DEV-Gordon/Agenturi-Django.git
```

### 3. Entrar en la carpeta del proyecto
```
cd Agenturi-Django
```

## Crear y activar el entorno virtual


### 1. Crear entorno virtual (dentro del proyecto)
```
python3 -m venv venv
```

### 2️. Activar entorno virtual
```
source venv/bin/activate
```
Cada vez que abras una nueva terminal, recuerda activar el entorno con:
```
source venv/bin/activate
```

## Instalar dependencias del proyecto

```
pip install --upgrade pip
pip install -r requirements.txt
```


## Preparar la base de datos (SQLite)


Aplica las migraciones necesarias para crear las tablas iniciales de Django:

```
python manage.py makemigrations
python manage.py migrate
```

## Ejecutar el servidor de desarrollo

```
python manage.py runserver
```

Luego, abre tu navegador y accede a:
http://127.0.0.1:8000/


## Autor

DEV-Gordon
Proyecto desarrollado con en Django sobre WSL.
