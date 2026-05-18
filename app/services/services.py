from ..models import Pedido
from ..repositories.repositories import (
    ClienteRepository,
    LocalRepository,
    PedidoRepository,
    RepartidorRepository,
)


class DashboardService:
    @staticmethod
    def build_metrics():
        return {
            'clientes': ClienteRepository().model.query.count(),
            'locales': LocalRepository().model.query.count(),
            'repartidores': RepartidorRepository().model.query.count(),
            'pedidos': PedidoRepository().model.query.count(),
            'pendientes': Pedido.query.filter_by(estado='Pendiente').count(),
            'en_ruta': Pedido.query.filter_by(estado='En ruta').count(),
            'entregados': Pedido.query.filter_by(estado='Entregado').count(),
        }


class PedidoService:
    VALID_STATES = ['Pendiente', 'Preparando', 'En ruta', 'Entregado', 'Cancelado']

    def __init__(self):
        self.pedido_repository = PedidoRepository()
        self.repartidor_repository = RepartidorRepository()

    def validate_payload(self, payload: dict):
        required = ['descripcion', 'direccion_entrega', 'total', 'cliente_id', 'local_id']
        for field in required:
            if not str(payload.get(field, '')).strip():
                raise ValueError(f'El campo {field} es obligatorio.')

        try:
            total = float(payload['total'])
        except ValueError as exc:
            raise ValueError('El total debe ser numérico.') from exc

        if total <= 0:
            raise ValueError('El total debe ser mayor que 0.')

        estado = payload.get('estado', 'Pendiente')
        if estado not in self.VALID_STATES:
            raise ValueError('El estado del pedido no es válido.')

    def create(self, payload: dict):
        self.validate_payload(payload)
        return self.pedido_repository.create(
            descripcion=payload['descripcion'].strip(),
            direccion_entrega=payload['direccion_entrega'].strip(),
            total=float(payload['total']),
            estado=payload.get('estado', 'Pendiente'),
            cliente_id=int(payload['cliente_id']),
            local_id=int(payload['local_id']),
            repartidor_id=int(payload['repartidor_id']) if payload.get('repartidor_id') else None,
        )

    def update(self, pedido, payload: dict):
        self.validate_payload(payload)
        return self.pedido_repository.update(
            pedido,
            descripcion=payload['descripcion'].strip(),
            direccion_entrega=payload['direccion_entrega'].strip(),
            total=float(payload['total']),
            estado=payload.get('estado', 'Pendiente'),
            cliente_id=int(payload['cliente_id']),
            local_id=int(payload['local_id']),
            repartidor_id=int(payload['repartidor_id']) if payload.get('repartidor_id') else None,
        )
