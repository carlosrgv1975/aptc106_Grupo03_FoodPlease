from datetime import datetime
from .extensions import db


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pedidos = db.relationship('Pedido', back_populates='cliente', cascade='all, delete')


class Local(db.Model):
    __tablename__ = 'locales'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    rubro = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pedidos = db.relationship('Pedido', back_populates='local', cascade='all, delete')


class Repartidor(db.Model):
    __tablename__ = 'repartidores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    vehiculo = db.Column(db.String(60), nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    pedidos = db.relationship('Pedido', back_populates='repartidor')


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), nullable=False, default='Pendiente')
    direccion_entrega = db.Column(db.String(255), nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    local_id = db.Column(db.Integer, db.ForeignKey('locales.id'), nullable=False)
    repartidor_id = db.Column(db.Integer, db.ForeignKey('repartidores.id'), nullable=True)

    cliente = db.relationship('Cliente', back_populates='pedidos')
    local = db.relationship('Local', back_populates='pedidos')
    repartidor = db.relationship('Repartidor', back_populates='pedidos')
