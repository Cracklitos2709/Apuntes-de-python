import sys
import math
# Factorial de 5 = 5 * 4 * 3 * 2 * 1

def factorial(numero): 
    """[Calcula el factorial de un numero]

    Args:
        numero ([Int]): [Cualquier valor entero]

        return el factorial de numero
    """

    if numero == 1:
        return 1
    return numero * factorial(numero - 1)

def run():
    numero = int(input('Introduce un numero entero\n'))
    print(f'El factorial de {numero} es {factorial(numero)}')
    print(sys.getrecursionlimit())


if __name__ == "__main__":
    run()

