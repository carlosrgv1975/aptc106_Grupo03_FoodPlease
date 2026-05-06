import sqlite3
from datetime import datetime

DATABASE = 'foodplease/foodplease.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class Pedido:
    @staticmethod
    def get_all():
        conn = get_db()
        pedidos = conn.execute('''
            SELECT p.*, c.nombre as cliente_nombre, l.nombre as local_nombre,
                   r.nombre as repartidor_nombre
            FROM pedidos p
            JOIN clientes c ON p.cliente_id = c.id
            JOIN locales l ON p.local_id = l.id
            LEFT JOIN repartidores r ON p.repartidor_id = r.id
        ''').fetchall()
        conn.close()
        return pedidos

    @staticmethod
    def get_by_id(id):
        conn = get_db()
        pedido = conn.execute('SELECT * FROM pedidos WHERE id = ?', (id,)).fetchone()
        conn.close()
        return pedido

    @staticmethod
    def create(cliente_id, local_id, repartidor_id, detalle, estado):
        conn = get_db()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.execute('INSERT INTO pedidos (cliente_id, local_id, repartidor_id, detalle, estado, fecha) VALUES (?, ?, ?, ?, ?, ?)',
                     (cliente_id, local_id, repartidor_id, detalle, estado, fecha))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id, cliente_id, local_id, repartidor_id, detalle, estado):
        conn = get_db()
        conn.execute('UPDATE pedidos SET cliente_id=?, local_id=?, repartidor_id=?, detalle=?, estado=? WHERE id=?',
                     (cliente_id, local_id, repartidor_id, detalle, estado, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        conn = get_db()
        conn.execute('DELETE FROM pedidos WHERE id = ?', (id,))
        conn.commit()
        conn.close()
