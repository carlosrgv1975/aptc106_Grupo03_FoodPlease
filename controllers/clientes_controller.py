from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes')
def index():
    clientes = Cliente.get_all()
    return render_template('clientes/index.html', clientes=clientes)

@clientes_bp.route('/clientes/nuevo', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        Cliente.create(request.form['nombre'], request.form['email'],
                       request.form['telefono'], request.form['direccion'])
        flash('Cliente creado exitosamente.', 'success')
        return redirect(url_for('clientes.index'))
    return render_template('clientes/form.html', cliente=None)

@clientes_bp.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def update(id):
    cliente = Cliente.get_by_id(id)
    if request.method == 'POST':
        Cliente.update(id, request.form['nombre'], request.form['email'],
                       request.form['telefono'], request.form['direccion'])
        flash('Cliente actualizado.', 'success')
        return redirect(url_for('clientes.index'))
    return render_template('clientes/form.html', cliente=cliente)

@clientes_bp.route('/clientes/eliminar/<int:id>')
def delete(id):
    Cliente.delete(id)
    flash('Cliente eliminado.', 'danger')
    return redirect(url_for('clientes.index'))
