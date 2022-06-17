print("Bienvenido al programa de una calculadora simple.\n")
num1 = input("Introduce el primer numero:")

while (num1.isdigit()==False):
    print("Introduce un valor numerico")
    num1 = input("Introduce el primer numero:")

operacion = input("Introduce la operacion que desea realizar (+ | - | * | /):")

while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "/":
    print("Introduce una Operacion valida!")
    operacion = input("Introduce la operacion que desea realizar (+ | - | * | /):")

num2 = input("Introduce el segundo numero:")

while (num2.isdigit()==False):
    print("Introduce un valor numerico")
    num2 = input("Introduce el segundo numero:")

num1 = float(num1)
num2 = float(num2)

try:
    if operacion == "+":
        print("La suma de ", num1,"+", num2," es de :",num1 + num2)

    elif operacion == "-":
        print("La resta de ", num1,"-", num2," es de :",num1 - num2)

    elif operacion == "*":
        print("La multiplicacion de ", num1,"*", num2," es de :",num1 * num2)

    elif operacion == "/":
        print("La division de ", num1,"/", num2," es de :",num1 / num2)

    else:
        print("La operacion no esta contemplada")
except ZeroDivisionError:
    print("No se puede divir entre cero!")

print("Gracias por usar el programa.")
