from flask import request
from models.Calculadora import Calculadora

calculadora = Calculadora()

class CalculadoraController:

    def saludo(self):
        return {"mensaje": "API de Calculadora funcionando"}

    def cuadrado(self, numero):

        resultado = calculadora.cuadrado(numero)

        return {
            "numero": numero,
            "resultado": resultado
        }

    def operacion(self):

        datos = request.json

        a = datos["a"]
        b = datos["b"]
        operacion = datos["operacion"]

        resultado = calculadora.operar(a, b, operacion)

        if isinstance(resultado, str):
            return {"error": resultado}

        return {
            "a": a,
            "b": b,
            "operacion": operacion,
            "resultado": resultado
        }