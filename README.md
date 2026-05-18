# FOODPLEASE — Aplicación CRUD Web

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-black.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-embedded-lightgrey.svg)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)](https://getbootstrap.com/)
[![Licencia académica](https://img.shields.io/badge/uso-acad%C3%A9mico-green.svg)]()

Aplicación CRUD web del proyecto **FoodPlease** construida en **Flask + SQLAlchemy + SQLite** con arquitectura por capas (Routes → Services → Repositories → Models). Gestiona clientes, locales comerciales, repartidores y pedidos a través de un panel administrativo, y deja preparada la base para integrar una aplicación móvil mediante API REST y desplegar en Cloud.

> **Asignatura:** APTC106 — Taller de Desarrollo Web y Móvil · **Universidad:** UNAB · **Grupo:** 03

---

## Tabla de contenidos

1. [Resumen del proyecto](#resumen-del-proyecto)
2. [Stack tecnológico](#stack-tecnológico)
3. [Arquitectura](#arquitectura)
4. [Requisitos previos](#requisitos-previos)
5. [Instalación y ejecución](#instalación-y-ejecución)
6. [Funcionalidades disponibles](#funcionalidades-disponibles)
7. [Estructura del repositorio](#estructura-del-repositorio)
8. [Datos seed](#datos-seed)
9. [Despliegue en Render](#despliegue-en-render)
10. [Roadmap y mejoras futuras](#roadmap-y-mejoras-futuras)
11. [Equipo](#equipo)

---

## Resumen del proyecto

FoodPlease es una plataforma de delivery que en su forma actual opera con asignación manual de pedidos, sin seguimiento en tiempo real ni integración entre actores (clientes, locales y repartidores). Este proyecto entrega el **panel administrativo web** que automatiza la gestión central del ecosistema y prepara el terreno para la posterior aplicación móvil del usuario final.

El sistema soporta:

- **Dashboard** con métricas operacionales (clientes, locales, repartidores, pedidos por estado).
- **CRUD completo** para las cuatro entidades del dominio.
- **Validaciones de negocio** centralizadas (estados válidos de pedido, total > 0, campos obligatorios).
- **Datos seed** para que cualquier evaluador pueda probar el sistema sin pasos manuales.

---

## Stack tecnológico

| Capa | Tecnología | Versión |
|------|------------|---------|
| Lenguaje | Python | 3.10+ |
| Framework web | Flask | 3.1.0 |
| ORM | Flask-SQLAlchemy | 3.1.1 |
| Persistencia | SQLite | embebida |
| Frontend | Jinja2 + Bootstrap | 5.3.3 (CDN) |
| Servidor de producción | Gunicorn (opcional) | — |

Stack deliberadamente austero, coherente con la filosofía *micro* de Flask. El proyecto se levanta sin servidores adicionales, sin builds y sin configuración previa más allá del entorno virtual.

---

## Arquitectura

El proyecto aplica una **arquitectura por capas** que combina tres patrones clásicos sobre la base MVC de Flask:

```
   Navegador (Bootstrap 5 + Jinja2)
              ↓
   Templates / Vistas      ← app/templates/*.html
              ↓
   Routes / Blueprints     ← app/routes/*.py        (HTTP, parsing, flash, redirect)
              ↓
   Services                ← app/services/services.py  (lógica de negocio)
              ↓
   Repositories            ← app/repositories/         (acceso a datos)
              ↓
   Models (SQLAlchemy ORM) ← app/models.py
              ↓
   SQLite (foodplease.db)
```

**Patrones aplicados:**

- **Application Factory Pattern** — `create_app()` instancia la app, registra Blueprints y datos seed.
- **Blueprints** — un módulo por dominio (Clientes, Locales, Repartidores, Pedidos, Main).
- **Repository Pattern** — `BaseRepository` genérico + repositorios concretos.
- **Service Layer** — validaciones y reglas de negocio aisladas (ver `PedidoService.VALID_STATES`).

Reglas duras de comunicación:
- Las **rutas** no tocan `db.session`.
- Los **repositorios** no leen `request.form`.
- Los **servicios** lanzan `ValueError` ante reglas incumplidas; las rutas los atrapan como `flash('danger')`.

---

## Requisitos previos

- **Python 3.10 o superior** ([descargar](https://www.python.org/downloads/))
- **pip** (incluido con Python)
- **Git** ([descargar](https://git-scm.com/downloads))
- Un navegador moderno (Chrome, Firefox, Edge, Safari)

Verificación rápida:

```bash
python --version    # debería mostrar 3.10 o superior
pip --version
git --version
```

---

## Instalación y ejecución

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/carlosrgv1975/aptc106_Grupo03_FoodPlease.git
cd aptc106_Grupo03_FoodPlease/foodplease_flask
```

### Paso 2 — Crear y activar el entorno virtual

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

### Paso 3 — Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4 — Ejecutar la aplicación

```bash
python run.py
```

La salida esperada es:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Paso 5 — Abrir en el navegador

Navega a [http://127.0.0.1:5000](http://127.0.0.1:5000) y verás el dashboard con los datos seed precargados.

> **Tiempo total estimado de instalación:** menos de 3 minutos en un equipo estándar.

---

## Funcionalidades disponibles

| Módulo | URL base | Operaciones |
|--------|----------|-------------|
| Dashboard | `/` | Métricas KPI + tabla de últimos pedidos |
| Clientes | `/clientes` | CRUD completo (nombre, teléfono, dirección) |
| Locales | `/locales` | CRUD completo (nombre, rubro, dirección) |
| Repartidores | `/repartidores` | CRUD + flag `disponible` (boolean) |
| Pedidos | `/pedidos` | CRUD + asociación cliente/local/repartidor + estados |

**Estados válidos para Pedido** (centralizados en `PedidoService.VALID_STATES`):

- `Pendiente` (estado por defecto)
- `Preparando`
- `En ruta`
- `Entregado`
- `Cancelado`

**Validaciones aplicadas en `PedidoService`:**

- Campos obligatorios: descripción, cliente, local, total.
- `total` debe ser numérico y mayor que 0.
- `estado` debe pertenecer a `VALID_STATES`.
- `repartidor_id` puede ser nulo (pedido sin asignar).

---

## Estructura del repositorio

```text
foodplease_flask/
├── run.py                       # Entry point (python run.py)
├── config.py                    # Configuración: URI BD, SECRET_KEY, BASE_DIR
├── requirements.txt             # Flask 3.1.0, Flask-SQLAlchemy 3.1.1
├── README.md                    # Este archivo
├── .gitignore                   # Excluye venv/, *.db, __pycache__/
└── app/
    ├── __init__.py              # Application Factory + register_blueprints + seed_data
    ├── extensions.py            # db = SQLAlchemy() singleton
    ├── models.py                # Cliente, Local, Repartidor, Pedido
    ├── routes/
    │   ├── main.py              # GET /  (dashboard)
    │   ├── clientes.py          # /clientes
    │   ├── locales.py           # /locales
    │   ├── repartidores.py      # /repartidores
    │   └── pedidos.py           # /pedidos
    ├── services/
    │   └── services.py          # DashboardService, PedidoService
    ├── repositories/
    │   ├── base_repository.py   # BaseRepository genérico (CRUD)
    │   └── repositories.py      # ClienteRepo, LocalRepo, RepartidorRepo, PedidoRepo
    ├── templates/
    │   ├── base.html            # Layout con navbar + flash messages
    │   ├── index.html           # Dashboard
    │   ├── clientes/
    │   │   ├── list.html        # Tabla con acciones
    │   │   └── form.html        # Formulario crear/editar
    │   ├── locales/
    │   ├── repartidores/
    │   └── pedidos/
    └── static/
        └── css/style.css        # Estilos mínimos (Bootstrap hace el grueso)
```

---

## Datos seed

Al primer arranque, `seed_data()` (en `app/__init__.py`) carga automáticamente:

- **2 clientes:** Luis Rojas, Ana Torres
- **2 locales:** Pizza Nova (pizzería), Burger Point (hamburguesería)
- **2 repartidores:** Diego Pérez (bicicleta), Camila Díaz (moto) — ambos disponibles
- **2 pedidos:** Pizza familiar pepperoni (en ruta), Combo hamburguesa + papas (pendiente)

Para regenerar los datos seed: detener la app, eliminar `instance/foodplease.db`, volver a ejecutar `python run.py`.

---

## Despliegue en Render

El proyecto está preparado para desplegarse en **Render** (free tier) en seis pasos:

1. Crear cuenta en [render.com](https://render.com) y conectar GitHub.
2. **New → Web Service**, seleccionar el repositorio.
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `gunicorn run:app` *(agregar `gunicorn` a `requirements.txt`)*
5. **Variables de entorno:** definir `SECRET_KEY` con un string aleatorio.
6. **Deploy** → URL pública disponible en pocos minutos.

> **Nota sobre persistencia:** el sistema de archivos de Render es efímero. Para producción real, migrar a la oferta gratuita de **PostgreSQL** de Render cambiando `SQLALCHEMY_DATABASE_URI` en `config.py`.

Alternativas evaluadas y descartadas: Railway (backup), PythonAnywhere (limitado), Heroku (sin free tier desde 2022). Comparativa completa en el informe del proyecto.

---

## Roadmap y mejoras futuras

| # | Mejora | Prioridad | Impacto |
|---|--------|-----------|---------|
| 1 | Autenticación con `Flask-Login` y roles (admin, local, repartidor, cliente) | Alta | Crítico para producción |
| 2 | API REST `/api/v1/*` para consumo desde la app móvil | Alta | Habilita la app móvil |
| 3 | Migraciones de esquema con `Flask-Migrate` (Alembic) | Media | Evolución sin reseed |
| 4 | Validaciones con `Flask-WTF` + protección CSRF | Media | Seguridad de formularios |
| 5 | Seguimiento en tiempo real con `Flask-SocketIO` | Media | Mejor UX cliente |
| 6 | Migración a PostgreSQL para producción | Media | Persistencia robusta |
| 7 | Tests automatizados con `pytest` + CI en GitHub Actions | Media | Confianza de cambios |
| 8 | Geolocalización del repartidor y enrutamiento | Baja | Diferenciador del producto |
| 9 | Notificaciones push para cambios de estado | Baja | Mejor experiencia móvil |

---

## Grupo de trabajo

**Grupo 03 — APTC106 Taller de Desarrollo Web y Movil — UNAB Online**

- Priscila Arganaraz
- Carlos Gonzalez Villegas
- Osvaldo Moncada
- Daniel Huerta

**Profesor:** Ernesto E. Vivanco T.

---

