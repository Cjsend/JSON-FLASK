from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Servidor Flask ativo!"})

@app.route('/saudar', methods=['POST'])
def saudar():
    dados = request.get_json() or {}
    nome = dados.get('nome') or 'visitante'
    return jsonify({"mensagem": f"Olá, {nome}! Bem-vindo ao servidor Flask!"})

@app.route('/dobro', methods=['POST'])
def dobro():
    dados = request.get_json() or {}
    numero = dados.get('numero')
    try:
        n = float(numero)
        resultado = n * 2
        # Retornar inteiro quando possível
        if resultado.is_integer():
            resultado = int(resultado)
        return jsonify({"resultado": resultado})
    except (TypeError, ValueError):
        return jsonify({"error": "Forneça um número válido em 'numero'"}), 400

if __name__ == '__main__':
    # Em produção, não use debug=True e utilize um servidor WSGI
    app.run(debug=True)
