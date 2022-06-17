from ejercicio3 import Calculadora


class CalculadoraX2(Calculadora):

    def sumar(self, x,y):
        self.resultado = x + y + y

    def restar(self, x,y):
        self.resultado = x - y - y

    def multiplicar(self, x,y):
        self.resultado = x * y * y

    def dividir(self, x,y):
        self.resultado = x / y / y
    

c1  = CalculadoraX2()
c1.dividir(10,2)

c1.mostrar_resultado()
