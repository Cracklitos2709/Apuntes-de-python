# Las funciones nos permiten modularisar el codigo

def sumar(numero_uno , numero_dos):
    return numero_uno + numero_dos


def nombre_completo(nombre, apellido, inverso = False):
    if inverso == False:
        return f'{nombre} {apellido}'
    else:
        return f'{apellido} {nombre}'

def run():
    numero_x = int(input('Introduce el valor de x\n'))
    numero_y = int(input('Introduce el valor de y\n'))

    print(sumar(numero_x,numero_y))

    nombre = input('Introduce tu nombre\n')
    apellido = input('Introduce tu apellido\n')
    print(nombre_completo(nombre, apellido))
    print(nombre_completo(nombre, apellido, inverso= True))
    print(nombre_completo(apellido= apellido,nombre= nombre))

run()




