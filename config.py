"""
Configuración de la aplicación FoodPlease.

Soporta dos entornos:
 - Desarrollo local: SQLite + SECRET_KEY por defecto.
 - Producción (Render Cloud): lee SECRET_KEY y DATABASE_URL desde variables de entorno.

En producción, Render inyectará SECRET_KEY como variable de entorno desde el panel.
Si en el futuro se agrega PostgreSQL, también vendrá como DATABASE_URL.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'foodplease.db'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-foodplease-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f'sqlite:///{DB_PATH}',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
