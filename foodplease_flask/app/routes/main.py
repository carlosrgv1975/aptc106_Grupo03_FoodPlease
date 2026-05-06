from flask import Blueprint, render_template

from ..models import Pedido
from ..services.services import DashboardService

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    metrics = DashboardService.build_metrics()
    ultimos_pedidos = Pedido.query.order_by(Pedido.fecha_creacion.desc()).limit(5).all()
    return render_template('index.html', metrics=metrics, ultimos_pedidos=ultimos_pedidos)
