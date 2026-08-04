from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

# Base de datos de la tripulación con emojis insignia
USUARIOS_AUTORIZADOS = {
    "1284": {"nombre": "Lester González 🏎️"},
    "9402": {"nombre": "Juan Milla 🎡"},
    "6159": {"nombre": "Osmedy Lopez 🧠"},
    "7230": {"nombre": "Osman Castro 🎲"},
    "8145": {"nombre": "Nery Rivera 🦎"},
    "1507": {"nombre": "Fernando Sanchez 🦾"},
    "3310": {"nombre": "Angel Flores 🏹"},
    "1717": {"nombre": "Carlos Maldonado 🦁"},
    "8362": {"nombre": "Alexy Garcia 🪐"},
    "5037": {"nombre": "Kevin Diaz 🍃"},
    "2918": {"nombre": "Olvin Ramirez 🤖"},
    "6749": {"nombre": "Usuario001 🐎"},
    "4005": {"nombre": "Erik Rosales ❄️"},
    "3180": {"nombre": "Williams Jimenez 🦕"},
    "9054": {"nombre": "Arnoldo Alvarenga 🤠"},
    "1301": {"nombre": "Jack Perdomo 🦈"},
    "3855": {"nombre": "Yeison Murillo 💀"},
    "4321": {"nombre": "Derick Carvajal 🔥"},
    "5863": {"nombre": "Kevin Pineda ⚔️"},
    "7410": {"nombre": "Milton Turcios 🐢"},
    "2004": {"nombre": "Angel Castillo 🐐"},
    "3455": {"nombre": "Josue Rivera 🪶"},
    "1928": {"nombre": "Josue Cruz 🐌"},
    "1734": {"nombre": "Libny Castillo 🕷️"},
    "3307": {"nombre": "Edwin Alvarado 👑"},
    "2711": {"nombre": "Yervi Mejia 🐯"},
    "8198": {"nombre": "Carlos García 🦅"},
    "5601": {"nombre": "Ever Murillo 🛸"},
    "8293": {"nombre": "Elder Cantarero ⛩️"},
    "4172": {"nombre": "Carlos Palma 🧢"},
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
