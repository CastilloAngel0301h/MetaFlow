from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

# Base de datos de la tripulación con emojis insignia
USUARIOS_AUTORIZADOS = {
    "2004": {"nombre": "Angel Castillo 🚢"},
    "5863": {"nombre": "Kevin Ramón Pineda ⚔️"},
    "8198": {"nombre": "Carlos David Garcia 🦅"},
    "1734": {"nombre": "Libny Castillo ⚡"},
    "4321": {"nombre": "Derick Alexander Carvajal 🔥"},
    "3455": {"nombre": "Josué Rivera 🌀"},
    "1301": {"nombre": "Jack Perdomo 🦈"},
    "2064": {"nombre": "Arnoldo Alvarenga 🤠"},
    "2711": {"nombre": "Yervi Mejia 🐯"},
    "3855": {"nombre": "Yeison Murillo 💀"},
    "5037": {"nombre": "Kevin Díaz 🍃"},
    "4005": {"nombre": "Erik Rosales ❄️"},
    "1507": {"nombre": "Fernando Sanchez 🦾"},
    "3307": {"nombre": "Edwin Alvarado 👑"},
    "3310": {"nombre": "Angel Flores 🏹"},
    "1800": {"nombre": "Usuario Invitado 🗺️"}
}

@app.route('/')
def home():
    # Sirve el archivo index.html directamente desde la misma carpeta
    return send_file('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    pin = data.get('pin', '').strip()
    
    usuario = USUARIOS_AUTORIZADOS.get(pin)
    if usuario:
        return jsonify({"success": True, "nombre": usuario['nombre']})
    else:
        return jsonify({"success": False, "message": "PIN incorrecto. Nivel de Ki insuficiente."}), 401

if __name__ == '__main__':
    # Ejecuta el servidor en el puerto 5000 (Asegúrate de que la indentación de este bloque de código sea de 4 espacios)
    app.run(host='0.0.0.0', port=5000, debug=True)
