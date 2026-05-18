from flask import Blueprint, flash, redirect, render_template, request, url_for

from ..repositories.repositories import LocalRepository

locales_bp = Blueprint('locales', __name__, url_prefix='/locales')
repo = LocalRepository()


@locales_bp.route('/')
def list_locales():
    return render_template('locales/list.html', locales=repo.get_all())


@locales_bp.route('/nuevo', methods=['GET', 'POST'])
def create_local():
    if request.method == 'POST':
        repo.create(
            nombre=request.form['nombre'],
            rubro=request.form['rubro'],
            direccion=request.form['direccion'],
        )
        flash('Local creado correctamente.', 'success')
        return redirect(url_for('locales.list_locales'))
    return render_template('locales/form.html', local=None)


@locales_bp.route('/<int:local_id>/editar', methods=['GET', 'POST'])
def edit_local(local_id):
    local = repo.get_by_id(local_id)
    if request.method == 'POST':
        repo.update(
            local,
            nombre=request.form['nombre'],
            rubro=request.form['rubro'],
            direccion=request.form['direccion'],
        )
        flash('Local actualizado correctamente.', 'success')
        return redirect(url_for('locales.list_locales'))
    return render_template('locales/form.html', local=local)


@locales_bp.route('/<int:local_id>/eliminar', methods=['POST'])
def delete_local(local_id):
    local = repo.get_by_id(local_id)
    repo.delete(local)
    flash('Local eliminado correctamente.', 'success')
    return redirect(url_for('locales.list_locales'))
