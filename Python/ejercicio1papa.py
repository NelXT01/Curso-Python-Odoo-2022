contador = 0
continuar = True
numero_guardado = "no hay número guardado"


def pedir_numero():
    global contador, continuar
    contador += 1
    try:
        if contador <= 3:
            numero_x = float(input("Ingrese un número: "))
            contador = 0
            return numero_x
        else:
            continuar = False
            return continuar
    except:
        if contador < 3:
            print("El dato ingresado no es un número."
                  "\nPor favor vuelta a intentarlo...")
            pedir_numero()
        elif contador == 3:
            print("El dato ingresado no es un número y se han acabado sus 3 intentos.")
            pedir_numero()
        else:
            contador = 0
            continuar = False
            print("Ha superado la cantidad de intentos.")
            return continuar


def pedir_operacion():
    global contador, continuar
    contador += 1
    try:
        if contador <= 3:
            operacion_x = input("Ingrese una operación: + , - , * , /  : ")
            if operacion_x == '+' or operacion_x == '-' or operacion_x == '*' or operacion_x == '/':
                contador = 0
                return operacion_x
            else:
                if contador <= 3:
                    print("Debe ingresar una operación válida.")
                    pedir_operacion()
                else:
                    contador = 0
                    continuar = False
                    return continuar
    except:
        if contador <= 3:
            print("No ha ingresado una operación válida. Por favor, vuelva a intentarlo.")
            pedir_operacion()
        else:
            contador = 0
            continuar = False
            return continuar


def realizar_operacion(parametro_nro1, parametro_nro2, parametro_operacion):
    resultado = 0
    if parametro_operacion == "+":
        resultado = parametro_nro1 + parametro_nro2
    elif parametro_operacion == "-":
        resultado = parametro_nro1 - parametro_nro2
    elif parametro_operacion == '*':
        resultado = parametro_nro1 * parametro_nro2
    elif parametro_operacion == '/':
        try:
            resultado = parametro_nro1 / parametro_nro2
        except:
            resultado = "No se puede realizar una división sobre cero"
    return resultado


while continuar:
    if type(numero_guardado) == str:
        numero1 = pedir_numero()
        if continuar:
            operacion_seleccionada = pedir_operacion()
            if continuar:
                numero2 = pedir_numero()
                if continuar:
                    resultado_final = realizar_operacion(numero1, numero2, operacion_seleccionada)
                    numero_guardado = resultado_final
                    print("\n", numero1, operacion_seleccionada, numero2, "=", resultado_final)
                    print("\n---------------------------------------------------------------")
                    desea_continuar = input("Ingrese la letra S para continuar: ").lower()
                    if desea_continuar != "s":
                        continuar = False
    else:
        numero1 = numero_guardado
        if continuar:
            operacion_seleccionada = pedir_operacion()
            if continuar:
                numero2 = pedir_numero()
                if continuar:
                    resultado_final = realizar_operacion(numero1, numero2, operacion_seleccionada)
                    numero_guardado = resultado_final
                    print("\n", numero1, operacion_seleccionada, numero2, "=", resultado_final)
                    print("\n---------------------------------------------------------------")
                    desea_continuar = input("Ingrese la letra S para continuar: ").lower()
                    if desea_continuar != "s":
                        continuar = False


print("Gracias por utilizar nuestro programa")




