from flask import Blueprint, jsonify, render_template
from random import choice
from .data import pokeneas

app_routes = Blueprint('routes', __name__)

@app_routes.route('/')
def home():
    return render_template('home.html')

@app_routes.route('/json')
def get_pokenea_json():
    pokenea = choice(pokeneas)
    pokenea["contenedor_id"] = "ID_DEL_CONTENEDOR"  # Temporal, reemplaza según sea necesario
    return jsonify(pokenea)

@app_routes.route('/html')
def show_pokenea():
    pokenea = choice(pokeneas)
    pokenea["contenedor_id"] = "ID_DEL_CONTENEDOR"  # Temporal, reemplaza según sea necesario
    return render_template('pokenea.html', pokenea=pokenea)
