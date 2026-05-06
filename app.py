import sys
sys.path.insert(0, '/content/foodplease')

from flask import Flask, render_template
from controllers.clientes_controller import clientes_bp
from controllers.locales_controller import locales_bp
from controllers.repartidores_controller import repartidores_bp
from controllers.pedidos_controller import pedidos_bp

app = Flask(__name__)
app.secret_key = 'foodplease_secret_key'

app.register_blueprint(clientes_bp)
app.register_blueprint(locales_bp)
app.register_blueprint(repartidores_bp)
app.register_blueprint(pedidos_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
