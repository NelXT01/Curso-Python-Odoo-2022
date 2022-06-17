
class Calculadora():
    def __init__(self):
        self.resultado = 0

    def sumar(self,x,y):
        resultado = x + y
        self.resultado = resultado

    def restar(self,x,y):
        resultado = x - y
        self.resultado = resultado

    def multiplicar(self,x,y):
        resultado = x * y
        self.resultado = resultado

    def dividir(self,x,y):
        resultado = x / y
        self.resultado = resultado

    def mostrar_resultado(self):
        print(self.resultado)
        

