from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..repositories.repositories import ClienteRepository

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')
repo = ClienteRepository()


@clientes_bp.route('/')
def list_clientes():
    return render_template('clientes/list.html', clientes=repo.get_all())


@clientes_bp.route('/nuevo', methods=['GET', 'POST'])
def create_cliente():
    if request.method == 'POST':
        repo.create(
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion'],
        )
        flash('Cliente creado correctamente.', 'success')
        return redirect(url_for('clientes.list_clientes'))
    return render_template('clientes/form.html', cliente=None)


@clientes_bp.route('/<int:cliente_id>/editar', methods=['GET', 'POST'])
def edit_cliente(cliente_id):
    cliente = repo.get_by_id(cliente_id)
    if request.method == 'POST':
        repo.update(
            cliente,
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion'],
        )
        flash('Cliente actualizado correctamente.', 'success')
        return redirect(url_for('clientes.list_clientes'))
    return render_template('clientes/form.html', cliente=cliente)


@clientes_bp.route('/<int:cliente_id>/eliminar', methods=['POST'])
def delete_cliente(cliente_id):
    cliente = repo.get_by_id(cliente_id)
    repo.delete(cliente)
    flash('Cliente eliminado correctamente.', 'success')
    return redirect(url_for('clientes.list_clientes'))
