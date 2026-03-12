from flask import jsonify

class CalculadoraView:

    def respuesta(self, data):
        return jsonify(data)