from funciones_calculadora import * 

a = None
b = None



flag_primero = False
flag_segundo = False
while True:
    match calculadora(a, b):
        case "1":
            a = int(input("Ingrese primer operando: "))
            print(f"Operando A: {a}")
            flag_primero = True
            flag_segundo = True
        case "2":
            if flag_primero:
             b = int(input("Ingrese segundo operando: "))
             print(f"Operando B: {b}")
             flag_primero = True
            else:
                print("Ingrese el primer operando...")
        case "3":
            if flag_primero and flag_segundo:
                match operacion(a,b):
                    case "a":
                        resultado = sumar(a,b)
                    case "b":
                        resultado = restar(a,b)
                    case "c":
                        resultado = multiplicar(a,b)
                    case "d":
                        if flag_segundo == 0:
                            print("Error Math...")
                        resultado = dividir(a,b)
                    case "e":
                        if flag_primero == 0:
                            resultado = 1
                        elif flag_segundo == 0:
                            resultadp = 1
                        resultado = factorial_ab(a,b)
                print("Operacion Exitosa...")
            elif flag_primero == False:
                print("Debe ingresar el primer operando... ")
            elif flag_segundo == False:
                print("Ingrese el segundo operando...")
        case "4":
            if flag_primero and flag_segundo:
                print(resultado)
        case "5":
            print("Saliendo...")
            break

            
            
                    
        
    input("Presione una tecla para continuar...")
