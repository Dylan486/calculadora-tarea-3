from flask import Flask
from controller.CalculadoraController import CalculadoraController
from views.CalculadoraView import CalculadoraView

app = Flask(__name__)

controller = CalculadoraController()
view = CalculadoraView()

@app.route('/saludo', methods=['GET'])
def saludo():
    return view.respuesta(controller.saludo())


@app.route('/cuadrado/<int:numero>', methods=['GET'])
def cuadrado(numero):
    return view.respuesta(controller.cuadrado(numero))


@app.route('/operacion', methods=['POST'])
def operacion():
    return view.respuesta(controller.operacion())


if __name__ == '__main__':
    app.run(debug=True)