def primera_letra_palabras(lista_palabras):
    primeras_letras = []
    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es un string'
        assert len(palabra) > 0, 'No se permiten los string vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras

def run():
    lista_palabras = ['Hola','Mundo','Python', 'Java']
    print(primera_letra_palabras(lista_palabras))

if __name__ == "__main__":
    run()