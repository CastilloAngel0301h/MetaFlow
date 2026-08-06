from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

# Base de datos de la tripulación con emojis insignia
USUARIOS_AUTORIZADOS = {
   
    "9876": {"nombre": "Usuario02 🐼"},
    "5020": {"nombre": "Usuario03 🦚"},
    "6014": {"nombre": "Usuario04 🦊"},
    "9018": {"nombre": "Usuario05 🧩"},
    "1467": {"nombre": "Usuario06 🎩"},
    "1566": {"nombre": "Usuario06 🕶️"},
    "6030": {"nombre": "Usuario10 🎸"},
    "1468": {"nombre": "Usuario08 📡"},
    "1745": {"nombre": "Usuario09 ⚽"},
    "4410": {"nombre": "Agente007 🪬="},
    "1800": {"nombre": "Dinia 🔪"}
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
