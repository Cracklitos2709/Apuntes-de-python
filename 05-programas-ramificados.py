# Programas ramificados == condicionales

# Operadores condicionales

# Operador de igualdad ==
print(5 == 5) # True 5 si es igual a 5
print(5 == 4) # False 5 no es igual a 4

# Operador de diferencia
print(5 != 10) # True 5 si es diferente de 10

# Operador mayor que y menor que
print(5 < 6) #True 5 si es menor a 6
print(5 > 4) #True 5 si es mayor a 4

# Operador mayor o igual y menor o igual
print(5 >= 5) # True 5 no es mayor que 5 pero si es igual
print(5 <= 5) # True 5 no es menor que 5 pero si es igual


# Operadores logicos

print(5 == 5 and 4 == 4) # True por que ambas condicionales se cumplen False si una no se cumple
print(5 < 4 or 5 == 5) # True por que al menos una de las dos condiciones se cumple
print(not True) # False por que el operador de negacion niega la condicion

# Ejercicio de practica 
edad = int(input('Introduce tu edad\n'))

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

if edad == 18:
    print('numeros iguales')
elif edad < 18:
    print('Numero menor')
elif edad > 18:
    print('Numero mayor')

# Condicional ternario

mensaje = 'Hola mundo' if 5 == 5 else 'Adios mundo'

print(mensaje)

# Reto
usuario = input('Como se llama el primer usuario\n')
usuario_edad = int(input('Cual es la edad del primer usuario\n'))
segundo_usuario = input('Como se llama el segundo usuario\n')
segundo_usuario_edad = int(input('Cual es la edad del segundo usuario\n'))

if usuario_edad > segundo_usuario_edad:
    print(f'{usuario} es mas grande que {segundo_usuario} por {usuario_edad - segundo_usuario_edad} anios')
else:
    print(f'{segundo_usuario} es mas grande que {usuario} por {segundo_usuario_edad - usuario_edad} anios')