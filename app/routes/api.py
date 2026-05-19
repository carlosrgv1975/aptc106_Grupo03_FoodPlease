"""
API REST v1 — FoodPlease
========================
Blueprint que expone los endpoints REST consumidos por la aplicación móvil
construida en Ionic + Angular. Mantiene la simetría con los Blueprints web:
reutiliza los mismos repositorios y servicios.

Reglas:
- Todas las respuestas son JSON.
- Los códigos HTTP siguen el estándar REST (200/201/204/400/404/500).
- Errores se devuelven con la forma {"error": "mensaje"} para que el frontend
  móvil pueda mostrarlos como toast.
"""

from flask import Blueprint, jsonify, request, abort
from ..models import Cliente, Local, Repartidor, Pedido
from ..repositories.repositories import (
    ClienteRepository,
    LocalRepository,
    RepartidorRepository,
    PedidoRepository,
)
from ..services.services import PedidoService, DashboardService

api_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')


# ---------------- Serializadores ----------------

def serialize_cliente(c: Cliente) -> dict:
    return {
        'id': c.id,
        'nombre': c.nombre,
        'telefono': c.telefono,
        'direccion': c.direccion,
        'created_at': c.created_at.isoformat() if c.created_at else None,
    }


def serialize_local(l: Local) -> dict:
    return {
        'id': l.id,
        'nombre': l.nombre,
        'rubro': l.rubro,
        'direccion': l.direccion,
        'created_at': l.created_at.isoformat() if l.created_at else None,
    }


def serialize_repartidor(r: Repartidor) -> dict:
    return {
        'id': r.id,
        'nombre': r.nombre,
        'telefono': r.telefono,
        'vehiculo': r.vehiculo,
        'disponible': r.disponible,
        'created_at': r.created_at.isoformat() if r.created_at else None,
    }


def serialize_pedido(p: Pedido, include_relations: bool = True) -> dict:
    data = {
        'id': p.id,
        'descripcion': p.descripcion,
        'estado': p.estado,
        'direccion_entrega': p.direccion_entrega,
        'total': p.total,
        'fecha_creacion': p.fecha_creacion.isoformat() if p.fecha_creacion else None,
        'cliente_id': p.cliente_id,
        'local_id': p.local_id,
        'repartidor_id': p.repartidor_id,
    }
    if include_relations:
        data['cliente'] = serialize_cliente(p.cliente) if p.cliente else None
        data['local'] = serialize_local(p.local) if p.local else None
        data['repartidor'] = serialize_repartidor(p.repartidor) if p.repartidor else None
    return data


# ---------------- Health check ----------------

@api_bp.route('/health', methods=['GET'])
def health():
    """Verificación rápida de que la API responde. Útil para CI/CD y Render healthcheck."""
    return jsonify({
        'status': 'ok',
        'service': 'FoodPlease API',
        'version': 'v1',
    })


# ---------------- Métricas (espejo del dashboard) ----------------

@api_bp.route('/metrics', methods=['GET'])
def metrics():
    """Métricas agregadas — espejo del dashboard web."""
    return jsonify(DashboardService.build_metrics())


# ---------------- Auth (versión simple para el prototipo) ----------------

@api_bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login simple para el prototipo: identifica al cliente por correo (campo opcional)
    o devuelve el primer cliente seed para demos. En producción se integraría con
    Flask-JWT-Extended; aquí mantenemos la simplicidad.
    """
    data = request.get_json(silent=True) or {}
    email_or_phone = data.get('email') or data.get('telefono') or ''

    cliente = None
    if email_or_phone:
        cliente = Cliente.query.filter_by(telefono=email_or_phone).first()
    if cliente is None:
        cliente = Cliente.query.first()  # Para demo: cae al primer cliente seed

    if cliente is None:
        return jsonify({'error': 'No hay clientes registrados.'}), 404

    return jsonify({
        'token': f'demo-token-{cliente.id}',  # Token mock — placeholder JWT
        'cliente': serialize_cliente(cliente),
    })


@api_bp.route('/auth/register', methods=['POST'])
def register():
    """Crea un cliente nuevo (alta de usuario en la app móvil)."""
    data = request.get_json(silent=True) or {}
    try:
        for field in ('nombre', 'telefono', 'direccion'):
            if not str(data.get(field, '')).strip():
                return jsonify({'error': f'El campo {field} es obligatorio.'}), 400
        cliente = ClienteRepository().create(
            nombre=data['nombre'].strip(),
            telefono=data['telefono'].strip(),
            direccion=data['direccion'].strip(),
        )
        return jsonify({
            'token': f'demo-token-{cliente.id}',
            'cliente': serialize_cliente(cliente),
        }), 201
    except Exception as exc:  # noqa: BLE001
        return jsonify({'error': str(exc)}), 500


# ---------------- Clientes ----------------

@api_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = ClienteRepository().get_all()
    return jsonify([serialize_cliente(c) for c in clientes])


@api_bp.route('/clientes/<int:cliente_id>', methods=['GET'])
def obtener_cliente(cliente_id):
    cliente = ClienteRepository().get_by_id(cliente_id)
    return jsonify(serialize_cliente(cliente))


# ---------------- Locales ----------------

@api_bp.route('/locales', methods=['GET'])
def listar_locales():
    locales = LocalRepository().get_all()
    return jsonify([serialize_local(l) for l in locales])


@api_bp.route('/locales/<int:local_id>', methods=['GET'])
def obtener_local(local_id):
    local = LocalRepository().get_by_id(local_id)
    return jsonify(serialize_local(local))


# ---------------- Repartidores ----------------

@api_bp.route('/repartidores', methods=['GET'])
def listar_repartidores():
    repartidores = RepartidorRepository().get_all()
    return jsonify([serialize_repartidor(r) for r in repartidores])


@api_bp.route('/repartidores/disponibles', methods=['GET'])
def listar_repartidores_disponibles():
    repartidores = RepartidorRepository().get_available()
    return jsonify([serialize_repartidor(r) for r in repartidores])


# ---------------- Pedidos ----------------

@api_bp.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = PedidoRepository().get_all()
    return jsonify([serialize_pedido(p) for p in pedidos])


@api_bp.route('/pedidos/<int:pedido_id>', methods=['GET'])
def obtener_pedido(pedido_id):
    pedido = PedidoRepository().get_by_id(pedido_id)
    return jsonify(serialize_pedido(pedido))


@api_bp.route('/pedidos/cliente/<int:cliente_id>', methods=['GET'])
def listar_pedidos_por_cliente(cliente_id):
    pedidos = Pedido.query.filter_by(cliente_id=cliente_id).order_by(Pedido.id.desc()).all()
    return jsonify([serialize_pedido(p) for p in pedidos])


@api_bp.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.get_json(silent=True) or {}
    try:
        pedido = PedidoService().create(data)
        return jsonify(serialize_pedido(pedido)), 201
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:  # noqa: BLE001
        return jsonify({'error': str(exc)}), 500


@api_bp.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def actualizar_pedido(pedido_id):
    pedido = PedidoRepository().get_by_id(pedido_id)
    data = request.get_json(silent=True) or {}
    try:
        pedido = PedidoService().update(pedido, data)
        return jsonify(serialize_pedido(pedido))
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:  # noqa: BLE001
        return jsonify({'error': str(exc)}), 500


@api_bp.route('/pedidos/<int:pedido_id>/estado', methods=['PATCH'])
def actualizar_estado_pedido(pedido_id):
    """Atajo para que la app móvil actualice solo el estado del pedido."""
    pedido = PedidoRepository().get_by_id(pedido_id)
    data = request.get_json(silent=True) or {}
    estado = data.get('estado', '')
    if estado not in PedidoService.VALID_STATES:
        return jsonify({'error': 'Estado no válido.',
                        'valid_states': PedidoService.VALID_STATES}), 400
    pedido.estado = estado
    from ..extensions import db
    db.session.commit()
    return jsonify(serialize_pedido(pedido))


@api_bp.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def eliminar_pedido(pedido_id):
    pedido = PedidoRepository().get_by_id(pedido_id)
    PedidoRepository().delete(pedido)
    return '', 204


# ---------------- Estados válidos (utilidad para la app móvil) ----------------

@api_bp.route('/pedidos/estados', methods=['GET'])
def listar_estados_validos():
    """La app móvil consume esta lista para renderizar el selector de estados."""
    return jsonify({'estados': PedidoService.VALID_STATES})
