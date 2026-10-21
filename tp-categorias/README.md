# Frontend - Gestión de Categorías (UTN TUPaD)

Aplicación web desarrollada con **React**, **TypeScript**, **Vite** y **Tailwind CSS** para el Trabajo Práctico de Programación IV (Unidad 6).

Consume la API REST desarrollada en FastAPI utilizando `fetch` nativo de JavaScript.

## 📋 Características Principales

* **Integración Full Stack:** CRUD completo de categorías conectado al backend en tiempo real.
* **Custom Hook (`useCategorias`):** Aislamiento de la lógica de negocio, manejo de estado (`useState`, `useEffect`) y peticiones HTTP.
* **Componentes:**
  * `Navbar`: Barra de navegación principal.
  * `CategoriaList`: Renderizado reactivo de la lista de categorías.
  * `CategoriaCard`: Tarjeta individual con acciones de edición y eliminación.
  * `CategoriaModal`: Formulario interactivo en modal para altas y modificaciones.
* **Tipado Estricto:** Tipos e interfaces definidos con TypeScript (`Categoria`).
* **Diseño:** Estilizado mediante clases de Tailwind CSS.
* **Configuración por Entorno:** Manejo de la URL base de la API a través de variables de entorno (`.env`).

---

## Requisitos Previos

* **Node.js** (v18 o superior)
* **npm** o **pnpm**
* Tener en ejecución el backend en `http://localhost:8000`

---

## Instalación y Ejecución

1. **Ubicarse en la carpeta del frontend:**
   ```powershell
   cd tp-categorias

2. **Instalar dependencias:**
   ```powershell
   npm install

3. **Configurar las variables de entorno:**
   Asegúrate de tener un archivo .env en la raíz de tp-categorias con el siguiente contenido:
   ```powershell
   VITE_API_URL=http://localhost:8000

3. **Iniciar el servidor de desarrollo:**
   Asegúrate de tener en ejecución también el backend en `http://localhost:8000`:
   ```powershell
   npm run dev