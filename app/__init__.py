from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa y registra el blueprint de las rutas
    from .routes import app_routes
    app.register_blueprint(app_routes)

    return app
