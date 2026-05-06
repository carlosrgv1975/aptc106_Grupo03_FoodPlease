from flask import Flask

from config import Config
from .extensions import db
from .models import Cliente, Local, Repartidor, Pedido
from .routes.main import main_bp
from .routes.clientes import clientes_bp
from .routes.locales import locales_bp
from .routes.repartidores import repartidores_bp
from .routes.pedidos import pedidos_bp


def seed_data():
    if Cliente.query.count() == 0:
        cliente_1 = Cliente(nombre='Ana Torres', telefono='+56 9 1234 5678', direccion='Av. Las Condes 123')
        cliente_2 = Cliente(nombre='Luis Rojas', telefono='+56 9 9876 5432', direccion='Providencia 456')

        local_1 = Local(nombre='Burger Point', rubro='Comida rápida', direccion='Ñuñoa 101')
        local_2 = Local(nombre='Pizza Nova', rubro='Pizzería', direccion='Santiago Centro 202')

        repartidor_1 = Repartidor(nombre='Camila Díaz', telefono='+56 9 3333 4444', vehiculo='Moto', disponible=True)
        repartidor_2 = Repartidor(nombre='Diego Pérez', telefono='+56 9 5555 6666', vehiculo='Bicicleta', disponible=True)

        db.session.add_all([cliente_1, cliente_2, local_1, local_2, repartidor_1, repartidor_2])
        db.session.commit()

        pedido_1 = Pedido(
            descripcion='Combo hamburguesa + papas',
            estado='Pendiente',
            direccion_entrega='Av. Apoquindo 1500',
            total=12990,
            cliente_id=cliente_1.id,
            local_id=local_1.id,
            repartidor_id=repartidor_1.id,
        )
        pedido_2 = Pedido(
            descripcion='Pizza familiar pepperoni',
            estado='En ruta',
            direccion_entrega='Los Leones 210',
            total=18990,
            cliente_id=cliente_2.id,
            local_id=local_2.id,
            repartidor_id=repartidor_2.id,
        )
        db.session.add_all([pedido_1, pedido_2])
        db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        seed_data()

    app.register_blueprint(main_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(locales_bp)
    app.register_blueprint(repartidores_bp)
    app.register_blueprint(pedidos_bp)

    return app
