import sqlite3

DATABASE = 'foodplease/foodplease.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Repartidor:
    @staticmethod
    def get_all():
        conn = get_db()
        repartidores = conn.execute('SELECT * FROM repartidores').fetchall()
        conn.close()
        return repartidores

    @staticmethod
    def get_by_id(id):
        conn = get_db()
        repartidor = conn.execute('SELECT * FROM repartidores WHERE id = ?', (id,)).fetchone()
        conn.close()
        return repartidor

    @staticmethod
    def create(nombre, telefono, vehiculo, disponible):
        conn = get_db()
        conn.execute('INSERT INTO repartidores (nombre, telefono, vehiculo, disponible) VALUES (?, ?, ?, ?)',
                     (nombre, telefono, vehiculo, disponible))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, nombre, telefono, vehiculo, disponible):
        conn = get_db()
        conn.execute('UPDATE repartidores SET nombre=?, telefono=?, vehiculo=?, disponible=? WHERE id=?',
                     (nombre, telefono, vehiculo, disponible, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db()
        conn.execute('DELETE FROM repartidores WHERE id = ?', (id,))
        conn.commit()
        conn.close()
