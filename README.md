# 📱 Mobile Inventory & Stock Management System (Flask)

Un sistema integral de gestión de inventario para dispositivos móviles desarrollado con **Flask** y **SQLAlchemy**. Esta aplicación permite administrar un ecosistema complejo de productos, integrando múltiples entidades relacionadas como fabricantes, proveedores, modelos y control de stock físico en almacén.

### 🛠️ Stack Tecnológico
* **Backend:** Python 3.x & Flask Framework.
* **Base de Datos:** MySQL / SQLAlchemy (ORM).
* **Gestión de DB:** Flask-Migrate para control de versiones de esquemas.
* **Frontend:** Jinja2 Templates & HTML5.

### 🌟 Arquitectura de Datos y Relaciones
El proyecto destaca por una estructura de base de datos relacional avanzada que incluye:
* **Entidades Relacionadas:** Gestión normalizada de Marcas, Modelos, Fabricantes y Proveedores.
* **Control de Stock:** Seguimiento detallado de unidades, incluyendo ubicación física (Letra y Número de Almacén).
* **Atributos Dinámicos:** Asociación de accesorios y características técnicas específicas para cada equipo.
* **Integridad Referencial:** Implementación de claves foráneas y eliminaciones en cascada (`ondelete='CASCADE'`).

### 🚀 Funcionalidades Principales
* **CRUD Multi-Nivel:** Gestión completa de dispositivos y marcas con validación de datos.
* **Lógica de Autocreación:** Sistema inteligente que detecta si un fabricante o modelo existe; si no, lo crea automáticamente al registrar un producto.
* **Panel Administrativo:** Interfaces para edición rápida de especificaciones y precios.
* **Manejo de Sesiones:** Uso de `flash messages` para feedback en tiempo real sobre acciones del usuario.

### 📁 Estructura del Proyecto
```
EFI-PARTE-I/
├── plantillas/      # Vistas dinámicas (Index, Marcas, Celulares, Edición)
├── instancia/       # Bases de datos locales de prueba (.db)
├── migraciones/     # Control de versiones del esquema SQL
├── aplicacion.py    # Lógica central, modelos de SQLAlchemy y Rutas
└── requisitos.txt   # Dependencias del proyecto
```

### ⚙️ Instalación
* **Clonar el repositorio.**

* **Configurar el entorno virtual e instalar dependencias:**
```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requisitos.txt
```

* **Configurar la base de datos:** El sistema utiliza MySQL. Asegúrate de configurar tu URI en app.config

* **Ejecutar:**
```
python aplicacion.py
```

Desarrollado por **Agustín Alejandro Fasano**
Técnico Superior en Desarrollo de Software
