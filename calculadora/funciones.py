def calculadora(a: int, b: int) -> int:
    import os
    os.system('clear')
    print(F"{'CALCULADORA':^50s}")
    print(f"Operando A: {a}")
    print(f"Operando B: {b}")
    print(f"{'Menu de Opciones':^50s}")
    print(f"1 - Ingresar primer operando (A)")
    print(f"2 - Ingresar segundo operando (B)")
    print("3 - Elegir Operacion")
    print("4 - Ver resultado")
    print("5 - Salir")
    return input("Ingrese opcion: ")

def sumar(a: int,b: int) -> int:
    """ Suma dos numeros enteros

    Args:
        a (int): Primer numero entero a sumar
        b (int): Segundo numero entero a sumar 

    Returns:
        int: Devuelve resultado de la suma
    """
    return a + b

def restar(a: int,b: int) -> int:
    """ Resta de dos numeros enteros

    Args:
        a (int): Primer numero entero
        b (int): Segundo numero enteto

    Returns:
        int: Devuelve resultado de la resta
    """
    return a - b

def multiplicar(a:int,b:int) -> int:
    """ Multiplica dos numeros enteros

    Args:
        a (int): Primer numero entero
        b (int): Segundo numero entero

    Returns:
        int: devuelve resultado de la multiplicacion
    """
    return a * b

def dividir(a:int,b:int) -> int:
    """ Division de dos numeros enteros

    Args:
        a (int): Dividendo
        b (int): Divisor

    Returns:
        int: Devuelve resultado de la division
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero...")

def factorial(a: int) -> int:
    """ Calcula el factorial de un numero entero

    Args:
        a (int): numero entero

    Returns:
        int: Devuelve el factorial de un numero entero
    """
    n = 1
    for i in range(2, a + 1):
        n *= i
    return n
    
def factorial_ab(a: int, b: int) -> int:
    """ Calcula el factorial de dos numeros enteros

    Args:
        a (int): Primer numero entero a calcular
        b (int): Segundo numero entero a calcular

    Returns:
        int: Devuelve el resultado del factorial de dos numeros enteros
    """
    resultado_a = factorial(a)
    resultado_b = factorial(b)
    return resultado_a, resultado_b


def operacion(a:int,b:int) -> int:
    """ Menu de Opciones

    Args:
        a (int): Primer numero entero ingresado
        b (int): Segundo numero entero ingresado

    Returns:
        int: Devuelve resultado de la operacion elegida
    """
    print(f"{'Menu de Opciones':^50s}")
    print("a - sumar")
    print("b - restar")
    print("c - multiplicar")
    print("d - dividir")
    print("e - factorial")
    opcion =  input("Igrese operacion: ")
    while opcion != "a" and opcion != "b" and opcion!= "c" and opcion != "d" and opcion != "e" :
        opcion = input("Ingrese una opcion valida: ")
    return opcion
        

