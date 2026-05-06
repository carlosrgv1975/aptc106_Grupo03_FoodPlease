from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.pedido import Pedido
from models.cliente import Cliente
from models.local import Local
from models.repartidor import Repartidor

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/pedidos')
def index():
    pedidos = Pedido.get_all()
    return render_template('pedidos/index.html', pedidos=pedidos)

@pedidos_bp.route('/pedidos/nuevo', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        local_id = request.form['local_id']
        repartidor_id = request.form['repartidor_id'] or None
        detalle = request.form['detalle']
        estado = request.form['estado']
        Pedido.create(cliente_id, local_id, repartidor_id, detalle, estado)
        flash('Pedido creado exitosamente.', 'success')
        return redirect(url_for('pedidos.index'))
    clientes = Cliente.get_all()
    locales = Local.get_all()
    repartidores = Repartidor.get_all()
    return render_template('pedidos/form.html', pedido=None,
                           clientes=clientes, locales=locales,
                           repartidores=repartidores)

@pedidos_bp.route('/pedidos/editar/<int:id>', methods=['GET', 'POST'])
def update(id):
    pedido = Pedido.get_by_id(id)
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        local_id = request.form['local_id']
        repartidor_id = request.form['repartidor_id'] or None
        detalle = request.form['detalle']
        estado = request.form['estado']
        Pedido.update(id, cliente_id, local_id, repartidor_id, detalle, estado)
        flash('Pedido actualizado.', 'success')
        return redirect(url_for('pedidos.index'))
    clientes = Cliente.get_all()
    locales = Local.get_all()
    repartidores = Repartidor.get_all()
    return render_template('pedidos/form.html', pedido=pedido,
                           clientes=clientes, locales=locales,
                           repartidores=repartidores)

@pedidos_bp.route('/pedidos/eliminar/<int:id>')
def delete(id):
    Pedido.delete(id)
    flash('Pedido eliminado.', 'danger')
    return redirect(url_for('pedidos.index'))
