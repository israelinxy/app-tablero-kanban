# 📊 App Kanban

Una aplicación de gestión de proyectos basada en el método Kanban, desarrollada con Django y Vue.js.

## 📋 ¿Qué es el Método Kanban?

El **método Kanban** es una metodología ágil para la gestión de proyectos que visualiza el flujo de trabajo mediante un tablero. Originado en la industria manufacturera, Kanban utiliza tarjetas para representar tareas y columnas para mostrar las etapas del proceso (como "Por Hacer", "En Progreso" y "Completado").En esencia, Kanban mejora la productividad y la colaboración en equipos.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: Vue.js 3 con Vite
- **Base de Datos**: SQLite (Recomendación: instalar y usar PostgreSQL)
- **Documentación API**: drf-spectacular
- **Autenticación**: JWT (JSON Web Tokens)

## 📁 Estructura del Proyecto

```
app-kanban/
├── backend/
│   ├── kanban_project/
│   ├── projects/
│   ├── tasks/
│   ├── manage.py
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .gitignore
├── LICENSE
└── README.md
```

- `backend/`: Contiene la API REST desarrollada con Django
  - `kanban_project/`: Aplicación principal del proyecto Django
  - `projects/`: Aplicación para gestionar proyectos
  - `tasks/`: Aplicación para gestionar tareas
- `frontend/`: Contiene la aplicación Vue.js (aún no implementada)

## 🚀 Requisitos

- Python 3.8+
- SQLite / PostgreSQL
- Node.js y npm

## 🔧 Configuración del Backend

1. Navega a la carpeta `backend/`:
   ```
   cd backend
   ```

2. Crea un entorno virtual:
   ```
   python -m venv env
   ```

3. Activa el entorno virtual:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

5. Configura la base de datos en `settings.py`

6. Ejecuta las migraciones:
   ```
   python manage.py migrate
   ```

7. Inicia el servidor:
   ```
   python manage.py runserver
   ```

## 🖥️ Uso

La aplicación permite gestionar proyectos y tareas utilizando un sistema Kanban. 

Para explorar la API y sus endpoints, puedes utilizar la documentación generada automáticamente por drf-spectacular:

1. Inicia el servidor Django
2. Navega a `http://localhost:8000/api/schema/swagger-ui/`

Esta interfaz proporciona una descripción detallada de todos los endpoints disponibles y permite probarlos directamente desde el navegador.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
