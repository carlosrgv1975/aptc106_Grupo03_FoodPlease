from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.repartidor import Repartidor

repartidores_bp = Blueprint('repartidores', __name__)

@repartidores_bp.route('/repartidores')
def index():
    repartidores = Repartidor.get_all()
    return render_template('repartidores/index.html', repartidores=repartidores)

@repartidores_bp.route('/repartidores/nuevo', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        Repartidor.create(request.form['nombre'], request.form['telefono'],
                          request.form['vehiculo'],
                          1 if request.form.get('disponible') else 0)
        flash('Repartidor creado exitosamente.', 'success')
        return redirect(url_for('repartidores.index'))
    return render_template('repartidores/form.html', repartidor=None)

@repartidores_bp.route('/repartidores/editar/<int:id>', methods=['GET', 'POST'])
def update(id):
    repartidor = Repartidor.get_by_id(id)
    if request.method == 'POST':
        Repartidor.update(id, request.form['nombre'], request.form['telefono'],
                          request.form['vehiculo'],
                          1 if request.form.get('disponible') else 0)
        flash('Repartidor actualizado.', 'success')
        return redirect(url_for('repartidores.index'))
    return render_template('repartidores/form.html', repartidor=repartidor)

@repartidores_bp.route('/repartidores/eliminar/<int:id>')
def delete(id):
    Repartidor.delete(id)
    flash('Repartidor eliminado.', 'danger')
    return redirect(url_for('repartidores.index'))
