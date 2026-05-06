import sqlite3

DATABASE = 'foodplease/foodplease.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS locales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            telefono TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS repartidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            vehiculo TEXT NOT NULL,
            disponible INTEGER DEFAULT 1
        );
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            local_id INTEGER NOT NULL,
            repartidor_id INTEGER,
            detalle TEXT NOT NULL,
            estado TEXT DEFAULT "pendiente",
            fecha TEXT DEFAULT (datetime("now")),
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (local_id) REFERENCES locales(id),
            FOREIGN KEY (repartidor_id) REFERENCES repartidores(id)
        );
    ''')
    conn.commit()
    conn.close()
    print("Base de datos creada ✅")
