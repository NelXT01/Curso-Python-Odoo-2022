op_usuario = True
res = 0

calculadora = "No hay datos"

def pedir_num():
    try:
        num1 =float(input("Introduce un numero:"))

        return num1

    except:
        print("Ingresa un valor numerico.")
        pedir_num()

    
def pedir_op():
    try:
        operacion =input("Ingrese 'Salir' para salir del programa.\nPara continuar...Ingrese una operacion( + | - | * | / ):")


        if operacion == "+" or operacion == "-" or operacion ==  "*" or operacion ==  "/":
            return operacion
        elif operacion.lower() == "salir":
            return "salir"

        else:

            print("No ha ingresado una operacion valida.") 
            pedir_op()
    except:
        print("La operacion no esta contemplada")
        pedir_op()
    
def calcular(num1, op, num2):
    try:
        print(num1, op ,num2)
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        else:
            if num2 == 0:
                print("No se puede dividir entre 0, no pierde su acumulado anterior")

                resultado = num1
            else:
                resultado = num1 / num2 
        print(num1, op, num2, "=", resultado)
        return resultado

    except:
        print("Error 404")
        return 0




while(op_usuario):

    if type(calculadora) == str:
        numero = pedir_num()
        ope = pedir_op()
        if ope == "salir":
            print("El total acumulado es: ", res)
            op_usuario = False
            break
        numero2 = pedir_num()
        print("-----------------")
        calculadora = calcular(numero, ope, numero2)
        res += calculadora

    else:
        numero = calculadora
        ope = pedir_op()
        if ope == "salir":
            print("-----------------")
            print("El total acumulado es: ", res)
            print("-----------------")
            op_usuario = False
            break
        numero2 = pedir_num()
        print("-----------------")
        calculadora = calcular(numero, ope, numero2)
        res += calculadora

print("Gracias por usar el programa.")


    
    


    
