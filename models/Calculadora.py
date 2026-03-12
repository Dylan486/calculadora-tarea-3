class Calculadora:

    def cuadrado(self, numero):
        return numero * numero

    def operar(self, a, b, operacion):

        if operacion == "suma":
            return a + b

        elif operacion == "resta":
            return a - b

        elif operacion == "multiplicacion":
            return a * b

        elif operacion == "division":

            if b == 0:
                return "No se puede dividir entre 0"

            return a / b

        else:
            return "Operacion no valida"