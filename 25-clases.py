class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f'Hola soy una persona me llamo {self.nombre}')

class Persona2(Persona): # Herencia en python
    def caminar(Self):
        print('Estoy caminando ...')


if __name__ == "__main__":
    carlos = Persona('Carlos')
    carlos.presentarse()
    

    jesus = Persona2('jesus')
    jesus.presentarse()
    jesus.caminar()