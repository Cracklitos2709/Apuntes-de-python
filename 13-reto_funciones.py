def numeracion_exaustiva(numero):
    respuesta = 0

    while respuesta ** 2 < numero:
        respuesta += 1

    if respuesta ** 2 == numero:
        print(f'La raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no tiene una raiz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.1
    paso  = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print('No se encontro la raiz cuadrada del objetivo')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo ) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada del objetivo es {respuesta}')




def run():
    objetivo = int(input('Introduce un numero entero por favor\n'))
    menu = '''
    
    1.Encontrar raiz cuadrada mediante numeracion exhaustiva
    2.Encontrar raiz cuadrada mediante aproximacion a soluciones
    3.Encontrar raiz cuadrada mediante busqueda binaria
    '''

    print(menu)

    opcion = int(input('Escoge una opcion\n'))

    if opcion == 1:
        numeracion_exaustiva(objetivo)
    elif opcion == 2:
        aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)


if __name__ == '__main__':
    run()