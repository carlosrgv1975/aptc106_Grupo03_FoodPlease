# FoodPlease CRUD con Flask

Proyecto CRUD web en **Flask + SQLite** adaptado al caso **FoodPlease**, tomando como base la propuesta del documento del equipo y orientado a cumplir el mínimo viable solicitado por la evaluación.

## Qué incluye

- Dashboard web para administración
- CRUD de **Clientes**
- CRUD de **Locales comerciales**
- CRUD de **Repartidores**
- CRUD de **Pedidos**
- Base de datos SQLite local
- Organización por capas simples:
  - `routes`: controlador / vistas web
  - `services`: reglas de negocio y validaciones
  - `repositories`: acceso a datos
  - `models`: entidades
- Datos de prueba automáticos

## Relación con la propuesta FoodPlease

La solución se ajusta al documento del caso, donde se plantea:

- una **plataforma web** para administración y supervisión
- gestión de **clientes**, **locales** y **repartidores**
- visualización del estado de **pedidos**
- centralización de información para toma de decisiones

En esta implementación, el foco del CRUD está en la parte web administrativa del ecosistema FoodPlease.

## Tecnologías

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5

## Estructura

```bash
foodplease_flask/
├── app/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   ├── templates/
│   ├── static/
│   ├── extensions.py
│   ├── models.py
│   └── __init__.py
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Instalación

### 1) Crear y activar entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### 2) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3) Ejecutar el proyecto

```bash
python run.py
```

### 4) Abrir en navegador

```text
http://127.0.0.1:5000
```

## Funcionalidad mínima viable

La aplicación cumple con un CRUD básico funcional porque permite:

- **Crear** registros
- **Listar** registros
- **Editar** registros
- **Eliminar** registros

Esto se aplica a los cuatro módulos principales del caso.

## Decisiones de diseño

### 1. Flask como framework web
Se eligió Flask porque permite construir un CRUD web simple, claro y desplegable localmente, que es exactamente el alcance mínimo solicitado.

### 2. SQLite para despliegue local
Se usó SQLite porque no requiere instalar un motor de base de datos externo, lo que facilita la ejecución por parte del docente y del equipo.

### 3. Separación por capas
Se incorporó una separación simple de responsabilidades:

- **Modelos**: representan entidades del dominio
- **Repositorios**: encapsulan acceso a datos
- **Servicios**: aplican validaciones y reglas mínimas
- **Rutas**: manejan la interacción HTTP y renderizado

Esto ayuda a cumplir con la parte de patrones y buenas prácticas.

### 4. Adaptación al caso FoodPlease
En vez de construir un CRUD genérico, se adaptó a la problemática del documento:

- pedidos
- clientes
- locales
- repartidores
- estados de entrega

### 5. Dashboard operativo
Se añadió un dashboard con métricas básicas para acercar la solución a la visión administrativa descrita en la propuesta del equipo.

## Sugerencias para el informe

Puedes documentar este proyecto con estas secciones:

1. Portada
2. Índice
3. Introducción
4. Análisis crítico de decisiones técnicas
5. Arquitectura propuesta
6. Descripción del CRUD web
7. Evidencia de funcionamiento local
8. Conclusiones
9. Bibliografía APA

## Posibles mejoras futuras

- autenticación por roles
- API REST para integración móvil
- notificaciones en tiempo real
- geolocalización de repartidores
- filtros y reportes avanzados
- despliegue en Render o Railway

