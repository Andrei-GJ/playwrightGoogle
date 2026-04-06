# Playwright Google Maps Scraper 🗺️🦷

Un script automatizado construido con Python, Playwright, y Pytest diseñado para extraer información pública de contacto desde Google Maps. Específicamente, este proyecto busca perfiles, omitiendo resultados patrocinados o lugares que ya tienen sitio web, para luego guardar los contactos localizados directo en una base de datos de PostgreSQL de forma asíncrona.

## 🚀 Características
- **Scraping Dinámico**: Hace scroll automáticamente para cargar más resultados locales y simula el clic en Google Maps.
- **Filtrado Inteligente**: Ignora resultados *"Patrocinados"* y lugares que ya tienen botón de *"Sitio Web"*.
- **Conformidad de Datos**: Limpia automáticamente los números de teléfono antes de subirlos a la base de datos.
- **Inserción Asíncrona**: Usa `threading` de Python para que la inserción de registros a la base de datos (Supabase) no bloquee el recorrido del scrapper.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **Scraping / Testing:** [Playwright](https://playwright.dev/python/) y [Pytest](https://docs.pytest.org/en/7.1.x/)
- **Base de Datos:** [PostgreSQL](https://www.postgresql.org/) (Alojado en Supabase)
- **ORM / Consultas:** [SQLAlchemy](https://www.sqlalchemy.org/)

---

## ⚙️ Configuración y Requisitos

### 1. Requerimientos del Sistema
Asegúrate de tener instalado Python 3.10 o superior y configurar un entorno virtual (muy recomendado).

### 2. Instalar Dependencias
Instala los paquetes necesarios corriendo el siguiente comando:
```bash
pip install pytest pytest-playwright pytest-base-url sqlalchemy python-dotenv psycopg2-binary
```

Una vez instalados los paquetes de Playwright, instala los navegadores necesarios ejecutando:
```bash
playwright install chromium
```

### 3. Configuración de Variables de Entorno (`.env`)
Debes crear un archivo **`.env`** en la carpeta principal del proyecto. Este archivo está ignorado por GitHub, así que es seguro.

Agrega la cadena de conexión de tu base de datos Supabase:
```env
DATABASE_URL="postgresql://usuario:contraseña@servidor.supabase.co:6543/postgres"
```

### 4. Configurar la Base de Datos (Supabase)
Asegúrate de tener una tabla llamada `contacts` con, al menos, la siguiente estructura:
- `id`: llave primaria
- `name`: Text o Varchar
- `phone`: Text o BIGINT *(No usar integer simple por el tamaño de los números colombianos)*
- `hasContact`: Boolean

---

## 💻 ¿Cómo funciona y cómo ejecutarlo?

La prueba automatizada está estructurada dentro de un suite the Pytest. 
Para ejecutar el scrapper de forma visible en pantalla (para que puedas ver la magia ocurriendo), ejecuta:

```bash
pytest -s
```
*(El uso de del flag `-s` en `pytest` permite capturar los prints por consola que se ejecutan durante la ejecución en vivo).*

Si te da problemas de entorno con el base url o quieres correr el script abriendo el navegador gráfico puedes añadir `--headed`:
```bash
pytest -s --headed
```

## 📂 Organización de Archivos Principales
* `index.py`: Script principal de la prueba Playwright (Punto de entrada de Pytest)
* `articlebundle/controller/articleController.py`: Lógica del scrapper, clics, y recolección inteligente de datos.
* `articlebundle/async_task/asynController.py`: Crea los hilos (threads) paralelos para guardar la data.
* `database/connect/dataBaseConnect.py`: Gestiona la conexión global SQLAlchemy al motor.
* `database/models/contacts.py`: Modelo final encargado del INSERT en SQL.