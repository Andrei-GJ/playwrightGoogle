# Playwright Google Maps Scraper

Automatización headless construida con Python, Playwright, SQLAlchemy y Pytest para extraer información pública de contacto desde Google Maps, filtrar resultados patrocinados o comercios que ya cuentan con sitio web y persistir los registros de forma asíncrona en PostgreSQL.

## Características

- **Scraping dinámico:** scroll automático sobre resultados locales e interacción programática con fichas de Google Maps.
- **Filtrado inteligente:** omite anuncios patrocinados y perfiles que ya disponen de sitio web propio.
- **Normalización de datos:** limpieza y saneamiento de números telefónicos antes de persistir en base de datos.
- **Inserción asíncrona:** uso de hilos (`threading`) para ejecutar las escrituras en PostgreSQL sin bloquear el recorrido de Playwright.

## Stack Tecnológico

- **Lenguaje:** Python 3.10+
- **Automatización y Runner:** Playwright, Pytest
- **Persistencia:** PostgreSQL (Supabase), SQLAlchemy

## Configuración y Ejecución

### 1. Entorno e instalación de dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### 2. Variables de entorno (`.env`)

Crea un archivo `.env` en la raíz del proyecto (ignorado por Git) con la cadena de conexión a PostgreSQL:

```env
DATABASE_URL="postgresql://usuario:contraseña@servidor.supabase.co:6543/postgres"
```

### 3. Esquema de base de datos

Tabla `contacts` en PostgreSQL:

- `id`: clave primaria
- `name`: `TEXT` / `VARCHAR`
- `phone`: `TEXT` / `BIGINT`
- `hasContact`: `BOOLEAN`

### 4. Ejecución

```bash
# Ejecución con salida por consola en vivo
pytest -s

# Ejecución con navegador visible
pytest -s --headed
```

## Estructura del Proyecto

- `index.py`: punto de entrada principal ejecutado por Pytest.
- `articlebundle/controller/articleController.py`: lógica de navegación, clics y extracción de datos.
- `articlebundle/async_task/asynController.py`: gestión de hilos paralelos para inserción en base de datos.
- `database/connect/dataBaseConnect.py`: configuración de la conexión global con SQLAlchemy.
- `database/models/contacts.py`: modelo relacional y operación de inserción en `contacts`.
