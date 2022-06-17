from ejercicio3 import Calculadora


class CalculadoraX2(Calculadora):

    def sumar(self, x,y):
        self.resultado = x + y + y

    def restar(self, x,y):
        self.resultado = x - y - y

    def multiplicar(self, x,y):
        self.resultado = x * y * y

    def dividir(self, x,y):
        try:
            resultado = x / y / y
            self.resultado = resultado
        except ZeroDivisionError:
            print("No se puede dividir entre cero!")
            
    
    

c1  = CalculadoraX2()
c1.dividir(10,0)

c1.mostrar_resultado()
