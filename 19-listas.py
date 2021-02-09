lista = [1,2,3,4,5]

for i in lista:
    print(i)

# Agrega el 6 al final de la lista
lista.append(6)
print(lista)

# Eliminar el 6 de la lista
lista.pop()
print(lista)

# Ordenar una lista de mayor a menor
lista.sort(reverse= True)
print(lista)

# Retornar una parte de la lista
indice = lista.index(2,0,5)
print(indice)

# Clonar una lista
nueva_lista = lista.copy()
print(nueva_lista)