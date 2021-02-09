# Algoritmo de enumeracion exhaustiva
# Encontrar la raiz cuadrada de un numero probando todas las posibilidades
numero = int(input('Introduce un numero entero por favor \n'))
respuesta = 0

while respuesta ** 2 < numero:
    print(respuesta)
    respuesta += 1

if respuesta ** 2 == numero:
    print(f'La raiz cuadrada de {numero} es {respuesta}')
else:
    print(f'{numero} no tiene una raiz cuadrada exacta')
