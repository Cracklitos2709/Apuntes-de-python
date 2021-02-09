# Tuplas es una lista de valores que no podemos cambiar

mi_tupla = (1,2,3,4,5,'abc',True)

# Tupla de un solo valor
tupla_sola = (1,)
print(type(tupla_sola))

# Desempaquetar una tupla
numeros = (1,2,3)
x,y,z = numeros
print(x)
print(y)
print(z)

# Regresar varios valores
def numeros():
    return (25,54)

print(numeros())
