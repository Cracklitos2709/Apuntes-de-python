# Iteraciones o ciclos 
# Permite repetir n veces una accion
# Break para salir del ciclo cuando una condicion se cumple

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
print('Fin del primer bucle')

contador_2 = 1
while True:
    print(contador_2)
    contador_2 += 1
    if contador_2 == 51:
        break
print('Fin del segundo bucle')

# Bucles anidados
contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1   
    contador_externo += 1
    contador_interno = 0