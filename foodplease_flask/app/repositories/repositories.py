from .base_repository import BaseRepository
from ..models import Cliente, Local, Repartidor, Pedido


class ClienteRepository(BaseRepository):
    model = Cliente


class LocalRepository(BaseRepository):
    model = Local


class RepartidorRepository(BaseRepository):
    model = Repartidor

    def get_available(self):
        return Repartidor.query.filter_by(disponible=True).order_by(Repartidor.nombre.asc()).all()


class PedidoRepository(BaseRepository):
    model = Pedido
