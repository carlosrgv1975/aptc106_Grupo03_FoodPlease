import sqlite3

DATABASE = 'foodplease/foodplease.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Cliente:
    @staticmethod
    def get_all():
        conn = get_db()
        clientes = conn.execute('SELECT * FROM clientes').fetchall()
        conn.close()
        return clientes

    @staticmethod
    def get_by_id(id):
        conn = get_db()
        cliente = conn.execute('SELECT * FROM clientes WHERE id = ?', (id,)).fetchone()
        conn.close()
        return cliente

    @staticmethod
    def create(nombre, email, telefono, direccion):
        conn = get_db()
        conn.execute('INSERT INTO clientes (nombre, email, telefono, direccion) VALUES (?, ?, ?, ?)',
                     (nombre, email, telefono, direccion))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, nombre, email, telefono, direccion):
        conn = get_db()
        conn.execute('UPDATE clientes SET nombre=?, email=?, telefono=?, direccion=? WHERE id=?',
                     (nombre, email, telefono, direccion, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db()
        conn.execute('DELETE FROM clientes WHERE id = ?', (id,))
        conn.commit()
        conn.close()
