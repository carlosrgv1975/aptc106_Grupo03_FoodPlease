from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.local import Local

locales_bp = Blueprint('locales', __name__)

@locales_bp.route('/locales')
def index():
    locales = Local.get_all()
    return render_template('locales/index.html', locales=locales)

@locales_bp.route('/locales/nuevo', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        Local.create(request.form['nombre'], request.form['direccion'],
                     request.form['categoria'], request.form['telefono'])
        flash('Local creado exitosamente.', 'success')
        return redirect(url_for('locales.index'))
    return render_template('locales/form.html', local=None)

@locales_bp.route('/locales/editar/<int:id>', methods=['GET', 'POST'])
def update(id):
    local = Local.get_b
