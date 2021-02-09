mi_diccionario = {
    'nombre': 'Carlos',
    'apellido': 'Galvan'
}

# Imprimir las llaves, valores o ambas cosas de un diccionario
for i in mi_diccionario.keys():
    print(i)
for i in mi_diccionario.values():
    print(i)
for i in mi_diccionario.items():
    print(i)

# Reasignar el valor de una llave
mi_diccionario['apellido'] = 'Kamey'

for i in mi_diccionario.items():
    print(i)

# Agregar nueva llave y valor al diccionario
mi_diccionario['edad'] = 19

for i in mi_diccionario.items():
    print(i)

# Borrar llave de un diccionario
del mi_diccionario['apellido']
for i in mi_diccionario.items():
    print(i)

# Saber si una llave existe dentro de un diccionario
print('nombre' in mi_diccionario)