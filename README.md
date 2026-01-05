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

