from flask import Flask
from app.routes import app_routes  # Importa tu Blueprint desde routes.py

app = Flask(__name__, template_folder = 'app/templates', static_folder='static')
app.register_blueprint(app_routes)  # Registra el Blueprint

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
