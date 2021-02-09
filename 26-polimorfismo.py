class Corredor:
    def __init__(self, nombre):
        self.nombre = nombre

    def correr(self):
        print(f'Soy {self.nombre} y estoy corriendo')

class Ciclista(Corredor):
    def correr(self):
        print(f'Soy {self.nombre} y estoy acelerando')


if __name__ == "__main__":
    carlos_corredor = Corredor('Carlos')
    carlos_corredor.correr()
    jesus_ciclista = Ciclista('Jesus')
    jesus_ciclista.correr()