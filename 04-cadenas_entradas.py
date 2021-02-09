cadena = 'Hola soy carlitos'
edad = 19

# Concatenar variables en python
print(f'{cadena} galvan {edad}')

# Multiplicar las cadenas con el operador *
print(f'{cadena} ' *3)

# Ver la cantidad de caracteres qque tiene mi cadena con len(cadena)
print(f'Caracteres: {len(cadena)}')

# Acceder a un caracter o elemento de mi cadena mediante el indice : cadena[int]
print(cadena[0])

# Obtener secciones de mi cadena o rebanadas mediante [inicio: final: forma_de_avanzar]
print(cadena[0:4:1])
print(cadena[5:8:1])
print(cadena[9:17:1])

# Podemos obtener secciones de la siguiente manera solo que esta forma guardara las partes en un vector
print(cadena.split(' '))

# Podemos remplazar una cadena del texto de la siguiente forma cadena.replace('palabra', 'nueva_palabra')
print(cadena.replace('carlitos', 'cracklitos'))

# Podemos voltear una cadena de la siguiente forma
print(cadena[::-1])
texto= 'luz azul'
print(texto[::-1])

# Entrada de informacion
# Recibimos informacion del usuario con la funcion input() esta funcion siempre nos regresa una cadena o dato string
nombre = input('Introduce tu nombre por favor\n')
# Si necesitamos pedirle un entero al usuario debemos de hacer castig de la siguiente manera int(input('mensaje'))
edad = int(input('Introduce tu edad\n'))

print(f'Hola {nombre} en el 2021 tendras {edad + 1}')