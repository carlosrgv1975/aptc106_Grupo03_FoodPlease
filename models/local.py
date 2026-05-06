import sqlite3

DATABASE = 'foodplease/foodplease.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Local:
    @staticmethod
    def get_all():
        conn = get_db()
        locales = conn.execute('SELECT * FROM locales').fetchall()
        conn.close()
        return locales

    @staticmethod
    def get_by_id(id):
        conn = get_db()
        local = conn.execute('SELECT * FROM locales WHERE id = ?', (id,)).fetchone()
        conn.close()
        return local

    @staticmethod
    def create(nombre, direccion, categoria, telefono):
        conn = get_db()
        conn.execute('INSERT INTO locales (nombre, direccion, categoria, telefono) VALUES (?, ?, ?, ?)',
                     (nombre, direccion, categoria, telefono))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, nombre, direccion, categoria, telefono):
        conn = get_db()
        conn.execute('UPDATE locales SET nombre=?, direccion=?, categoria=?, telefono=? WHERE id=?',
                     (nombre, direccion, categoria, telefono, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db()
        conn.execute('DELETE FROM locales WHERE id = ?', (id,))
        conn.commit()
        conn.close()
