import math
numero = int(input('Introduce un numero entero\n'))
contador = 0

while contador ** 2 < numero:
    contador += 1
if contador ** 2 == numero:
    print(f'La raiz exacta de {numero} es {contador}')
else:
    print(f'{numero} no tiene una raiz exacta, la raiz de {numero} es {math.sqrt(numero)}')