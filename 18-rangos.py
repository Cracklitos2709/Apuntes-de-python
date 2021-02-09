# Range(comienzo,final,pasos)

numeros = list(range(0,11,2))
print(numeros)

# Comparar objetos
print(range(1,11,1) is range(1,11,1))

# Numeros pares
for i in range(0,101,2):
    print(i)

# Numeros impares
for i in range(0,101):
    if i % 2 != 0:
        print(i)