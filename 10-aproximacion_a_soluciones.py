# Encontrar la raiz de un numero aunque sea aproximada
objetivo = int(input('Introduce un numero\n'))
epsilon = 0.1
paso  = epsilon ** 2
respuesta = 0.0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta ** 2 - objetivo))
    respuesta += paso
if abs(respuesta ** 2 - objetivo) >= epsilon:
    print('No se encontro la raiz cuadrada del objetivo')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')