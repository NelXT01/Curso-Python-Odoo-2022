
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
        try:
            resultado = x / y
            self.resultado = resultado
        except ZeroDivisionError:
            print("No se puede dividir entre cero!")

    def mostrar_resultado(self):
        print(self.resultado)
        

c1 = Calculadora()

c1.dividir(10,2)
c1.mostrar_resultado()