# Instalación

Crear entorno virtual y ejecutar:

```
pip install django
```

# Inicialización

## Crear proyecto

```
django-admin startproject [nombre del módulo] [carpeta]
```

```
django-admin startproject core tutorialproject 
```

Esto crea la carpeta core, donde tendremos la configuración del proyecto:

```
core/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

- `urls.py`: rutas

## Aplicación

Una buena práctica es crear un módulo por cada caso de uso. Nos ubicamos dentro de la carpeta del proyecto

```
cd tutorialproject
```

Y ejecutamos:

```
django-admin startapp todos
```

Esto crea la carpeta todos con los archivos básicos para la aplicación (caso de uso):

```
todos/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
    └── __init__.py
```

- `views.py`: vistas (HTTP y respuestas JSON)

Para registrar la aplicación dentro del proyecto, dentro de settings.py (de core), en `INSTALLED_APPS` añadimos la aplicación `todos`:

```
INSTALLED_APPS = [
    ...
    'todos',
]
```

# Iniciar servidor

Desde dentro de la carpeta del proyecto (`tutorialproject`):

```
python manage.py runserver
```

Es un servidor de desarrollo, lo que significa:

- NO USAR EN PRODUCCIÓN: no es un servidor optimizado en materia de seguridad para usar en un entorno de producción
- No es necesario reiniciar para ver cambios

# Gunicorn

El servidor de Django únicamente nos sirve para desarrollo, ya que no está optimizado para gestionar concurrencia, volúmen, seguridad, etc. En un entorno de producción debemos usar otro 

## Instalación

```
pip install gunicorn
```

## Ejecución

```
gunicorn core.wsgi:application
```

Si hay un problema de CSS (en especial con la ruta /admin):

1. En `settings.py` añadimos:

   ```python
   import os
   PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
   STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
   ```

2. Ejecutar `python manage.py collectstatic`, lo que llevará los archivos estáticos

