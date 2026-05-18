from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..repositories.repositories import ClienteRepository, LocalRepository, PedidoRepository, RepartidorRepository
from ..services.services import PedidoService

pedidos_bp = Blueprint('pedidos', __name__, url_prefix='/pedidos')
pedido_repo = PedidoRepository()
cliente_repo = ClienteRepository()
local_repo = LocalRepository()
repartidor_repo = RepartidorRepository()
service = PedidoService()


def _load_context():
    return {
        'clientes': cliente_repo.get_all(),
        'locales': local_repo.get_all(),
        'repartidores': repartidor_repo.get_all(),
        'estados': service.VALID_STATES,
    }


@pedidos_bp.route('/')
def list_pedidos():
    return render_template('pedidos/list.html', pedidos=pedido_repo.get_all())


@pedidos_bp.route('/nuevo', methods=['GET', 'POST'])
def create_pedido():
    context = _load_context()
    if request.method == 'POST':
        try:
            service.create(request.form)
            flash('Pedido creado correctamente.', 'success')
            return redirect(url_for('pedidos.list_pedidos'))
        except ValueError as exc:
            flash(str(exc), 'danger')
    return render_template('pedidos/form.html', pedido=None, **context)


@pedidos_bp.route('/<int:pedido_id>/editar', methods=['GET', 'POST'])
def edit_pedido(pedido_id):
    pedido = pedido_repo.get_by_id(pedido_id)
    context = _load_context()
    if request.method == 'POST':
        try:
            service.update(pedido, request.form)
            flash('Pedido actualizado correctamente.', 'success')
            return redirect(url_for('pedidos.list_pedidos'))
        except ValueError as exc:
            flash(str(exc), 'danger')
    return render_template('pedidos/form.html', pedido=pedido, **context)


@pedidos_bp.route('/<int:pedido_id>/eliminar', methods=['POST'])
def delete_pedido(pedido_id):
    pedido = pedido_repo.get_by_id(pedido_id)
    pedido_repo.delete(pedido)
    flash('Pedido eliminado correctamente.', 'success')
    return redirect(url_for('pedidos.list_pedidos'))
