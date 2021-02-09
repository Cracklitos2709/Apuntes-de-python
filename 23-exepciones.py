def division(lista,divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return 'Estas tratando de dividir entre cero lo cual es un error'



lista = list(range(1,11))
divisor = 0

print(division(lista , divisor))


