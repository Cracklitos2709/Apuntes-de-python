variable_x = 100 # Scope global

def sumar():
    variable_y = 100 # Scope local por que esta dentro de la funcion, solo existe dentro de la funcion
    return variable_x + variable_y

print(sumar())
print(f'Variable x = {variable_x}')
# print(f'Variable y = {variable_y}') esto no es posible ya que estamos fuera de la funcion y variable_y solo existe dentro de esta

