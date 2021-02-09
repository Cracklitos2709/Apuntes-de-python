def decorador(funcion):
    def funcion_interna():
        print('Realizando operacion ...')
        funcion()
        print(f'Operacion terminada !')
    return funcion_interna()

@decorador
def suma():
    print(25 + 25)

