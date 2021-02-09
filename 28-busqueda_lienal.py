import random

def busqueda_lineal(lista,objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    longitud_lista = int(input('Cual es el tamano de la lista\n'))
    objetivo = int(input('Cual es el objetivo\n'))

    lista = [random.randint(0,100) for i in range(longitud_lista)]

    print(lista)
    
    if busqueda_lineal(lista,objetivo) == True:
        print(f'El elemento {objetivo} si esta en la lista')
    else:
        print(f'El elemento {objetivo} no esta en la lista')
