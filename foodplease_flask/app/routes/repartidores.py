from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..repositories.repositories import RepartidorRepository

repartidores_bp = Blueprint('repartidores', __name__, url_prefix='/repartidores')
repo = RepartidorRepository()


@repartidores_bp.route('/')
def list_repartidores():
    return render_template('repartidores/list.html', repartidores=repo.get_all())


@repartidores_bp.route('/nuevo', methods=['GET', 'POST'])
def create_repartidor():
    if request.method == 'POST':
        repo.create(
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            vehiculo=request.form['vehiculo'],
            disponible='disponible' in request.form,
        )
        flash('Repartidor creado correctamente.', 'success')
        return redirect(url_for('repartidores.list_repartidores'))
    return render_template('repartidores/form.html', repartidor=None)


@repartidores_bp.route('/<int:repartidor_id>/editar', methods=['GET', 'POST'])
def edit_repartidor(repartidor_id):
    repartidor = repo.get_by_id(repartidor_id)
    if request.method == 'POST':
        repo.update(
            repartidor,
            nombre=request.form['nombre'],
            telefono=request.form['telefono'],
            vehiculo=request.form['vehiculo'],
            disponible='disponible' in request.form,
        )
        flash('Repartidor actualizado correctamente.', 'success')
        return redirect(url_for('repartidores.list_repartidores'))
    return render_template('repartidores/form.html', repartidor=repartidor)


@repartidores_bp.route('/<int:repartidor_id>/eliminar', methods=['POST'])
def delete_repartidor(repartidor_id):
    repartidor = repo.get_by_id(repartidor_id)
    repo.delete(repartidor)
    flash('Repartidor eliminado correctamente.', 'success')
    return redirect(url_for('repartidores.list_repartidores'))
