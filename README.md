<p align="center">
  <img src="Home/static/Home/img/portada_github.png" alt="Coffee Organic Life" width="100%">
</p>

# Blog - Plataforma Web Django

Un proyecto Django completo que integra un blog educativo con módulos de aprendizaje, contacto y una página de inicio.

## 📋 Descripción

Este proyecto es una plataforma web construida con Django que proporciona:

- **Página de Inicio (Home)**: Landing page principal con diseño responsivo
- **Plataforma de Aprendizaje (Learning)**: Módulo para gestionar cursos y libros con subcategorías
- **Formulario de Contacto**: Sistema de contacto para usuarios
- **Panel de Administración**: Interfaz admin de Django para gestionar contenido

## 🛠️ Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

## 📦 Instalación

### 1. Clonar o descargar el repositorio

```bash
git clone <URL-del-repositorio>
cd Blog
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

Activar el entorno virtual:

**En Windows:**
```bash
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

```bash
python manage.py migrate
```

### 5. Crear un superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en consola para crear tu cuenta de administrador.

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El proyecto estará disponible en `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
Blog/
├── Blog/                      # Configuración principal del proyecto
│   ├── settings.py           # Configuración de Django
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuración WSGI
│   └── __init__.py
│
├── Home/                      # App de página de inicio
│   ├── templates/Home/       # Templates HTML
│   │   ├── index.html        # Página principal
│   │   └── Base/
│   │       └── base.html     # Template base
│   ├── static/Home/          # Archivos estáticos
│   │   └── css/
│   │       ├── style.css
│   │       └── responsive.css
│   ├── views.py              # Vistas
│   ├── urls.py               # URLs de Home
│   └── models.py             # Modelos de datos
│
├── Learning/                  # App de plataforma educativa
│   ├── templates/Learning/   # Templates HTML
│   │   ├── cours/            # Sección de cursos
│   │   │   ├── cours.html
│   │   │   └── subcategory_cours.html
│   │   └── books/            # Sección de libros
│   │       ├── books.html
│   │       └── subcategory_books.html
│   ├── static/Learning/css/  # Estilos CSS
│   ├── views.py              # Vistas
│   ├── urls.py               # URLs de Learning
│   ├── models.py             # Modelos de datos
│   └── migrations/           # Migraciones de BD
│
├── Contact/                   # App de contacto
│   ├── templates/Contact/   # Templates HTML
│   │   └── contacto.html    # Formulario de contacto
│   ├── static/Contact/css/  # Estilos CSS
│   ├── views.py             # Vistas
│   ├── urls.py              # URLs de Contact
│   ├── forms.py             # Formularios
│   └── models.py            # Modelos de datos
│
├── media/                     # Archivos multimedia subidos por usuarios
│   └── learning/
│
├── db.sqlite3                # Base de datos SQLite
├── manage.py                 # Script de gestión de Django
└── requirements.txt          # Dependencias del proyecto
```

## 🚀 Uso

### Acceder al Panel de Administración

1. Ve a `http://127.0.0.1:8000/admin/`
2. Inicia sesión con tus credenciales de superusuario
3. Gestiona contenido de las diferentes aplicaciones

### Rutas Principales

| Ruta | Descripción |
|------|-------------|
| `/` | Página de inicio |
| `/Learning/` | Plataforma de aprendizaje |
| `/Contact/` | Formulario de contacto |
| `/admin/` | Panel de administración |

## 📦 Dependencias

- **Django==2.2.3** - Framework web
- **django-crispy-forms==1.14.0** - Renderizado de formularios
- **Pillow==8.4.0** - Procesamiento de imágenes
- **psycopg2==2.8.6** - Adaptador PostgreSQL
- **gunicorn==20.1.0** - Servidor WSGI para producción
- **whitenoise==5.3.0** - Servicio de archivos estáticos en producción
- **pytz==2021.3** - Manejo de zonas horarias
- **sqlparse==0.4.2** - Parser SQL

## 🔧 Configuración Importante

### En Producción

Antes de desplegar a producción:

1. **Cambiar la SECRET_KEY** en `Blog/settings.py`
2. **Establecer DEBUG = False**
3. **Actualizar ALLOWED_HOSTS** con los dominios permitidos
4. **Usar una base de datos robusta** (PostgreSQL en lugar de SQLite)
5. **Configurar variables de entorno** para información sensible

### Variables de Entorno (Recomendado)

Crear un archivo `.env` en la raíz del proyecto:

```
SECRET_KEY=tu-clave-secreta
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/blog_db
```

## 📝 Comandos Útiles de Django

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar tests
python manage.py test

# Crear app nueva
python manage.py startapp nombre_app

# Recopilar archivos estáticos (producción)
python manage.py collectstatic
```

## 🌐 Despliegue

Este proyecto puede ser desplegado en plataformas como:

- **Heroku**
- **PythonAnywhere**
- **AWS (EC2, Elastic Beanstalk)**
- **DigitalOcean**
- **Google Cloud Platform**
- **Servidor VPS propio**

Requiere ajustar `settings.py` según el entorno específico.

## 📧 Contacto y Soporte

Para reportar problemas o sugerencias, utiliza el formulario de contacto en la aplicación o contacta directamente con el equipo de desarrollo.

## 📄 Licencia

Este proyecto es de codigo abierto.

---

**Última actualización:** Diciembre 2025

**Versión del Proyecto:** 1.0
