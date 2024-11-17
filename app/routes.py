from flask import Blueprint, jsonify, render_template
from random import choice
import os
from .data import pokeneas  # Importa la lista de datos

app_routes = Blueprint('routes', __name__)

@app_routes.route('/')
def home():
    return render_template('home.html')

@app_routes.route('/json')
def get_pokenea_json():
    if not pokeneas:  # Verificar si la lista está vacía
        return jsonify({"error": "No hay datos de Pokeneas disponibles"}), 404
    
    pokenea = choice(pokeneas)
    container_id = os.getenv('HOSTNAME', 'unknown')  # Obtiene el valor de la variable de entorno HOSTNAME
    pokenea["contenedor_id"] = container_id
    return jsonify(pokenea)

@app_routes.route('/html')
def show_pokenea():
    if not pokeneas:  # Verificar si la lista está vacía
        return render_template('error.html', message="No hay datos de Pokeneas disponibles")  # Asegúrate de tener una plantilla 'error.html'
    
    pokenea = choice(pokeneas)
    container_id = os.getenv('HOSTNAME', 'unknown')  # Obtiene el valor de la variable de entorno HOSTNAME
    pokenea["contenedor_id"] = container_id
    return render_template('pokenea.html', pokenea=pokenea)
