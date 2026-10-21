# API REST - Gestión de Productos y Categorías (UTN TUPaD)

Backend desarrollado con **FastAPI**, **SQLModel / SQLAlchemy** y **SQLite** para el Proyecto de la Unidad 6 de Programación IV.

## 📋 Características Principales
* **Arquitectura Modular:** Separación clara por dominios (`categoria` y `producto`).
* **Relación Many-to-Many:** Tabla intermedia `ProductoCategoria` con borrado en cascada (`ondelete="CASCADE"`).
* **Seed Automático:** Inicialización de la base de datos con datos de prueba al arrancar la aplicación si está vacía.
* **CORS Habilitado:** Configurado para la integración fluida con frontend en React (Vite).
* **Consultas Avanzadas:** *Eager Loading* con `selectinload` para endpoint detallado.

---

## ⚙️ Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio y ubicarse en la carpeta del backend:**
   ```powershell
   cd fastapi-productos

2. **Instalar las dependencias:**
   ```powershell
   pip install -r requirements.txt

3. **Ejecutar la aplicación (con FastAPI CLI):**
    Es importante tenerlo en el PATH en variables de entorno. 
   ```powershell
   fastapi dev app/main.py

