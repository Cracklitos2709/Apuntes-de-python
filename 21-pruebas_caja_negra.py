import unittest
def suma(x,y):
    return x + y

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 10
        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 20)


    def test_suma_negativos(self):
        num_1 = -5
        num_2 = -5
        resutaldo = suma(num_1,num_2)

        self.assertEqual(resutaldo, -10)



if __name__ == "__main__":
    unittest.main()