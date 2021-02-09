import random

def busqueda_binaria(lista, inicio,final, objetivo):
    if inicio > final:
        return False
    medio = (inicio + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)

if __name__ == "__main__":
    longitud_lista = int(input('Cual es el tamano de la lista\n'))
    objetivo = int(input('Cual es el objetivo\n'))

    lista = sorted([random.randint(0,100) for i in range(longitud_lista)])

    print(lista)

    if busqueda_binaria(lista, 0 , len(lista), objetivo) == True:
        print(f'El elemento {objetivo} si esta en la lista')
    else:
        print(f'El elemento {objetivo} no esta en la lista')