# Las variables en python deben de tener un nombre que sea explicativo y ademas debe de llevar la sigueinte forma nombre_variable

# literales
literales = [1,'abc',2.0,True]

# literal operador literal

print(1 + 2)
print(1 * 2)
print(1 / 2)
print(1 - 1)
print(10 % 2)

# Forma correcta de nombrar las variables para calcular el area de un triangulo
base = 10
altura = 10
area = base * altura
print(f'El area del triangulo es {area}')

# Las variables se pueden sobreescribir aunque en realidad apuntan a otro espacio en memoria y el espacio anterior es borrado
base = 15
altura = 15
print(f'El area del triangulo es {base * altura}')