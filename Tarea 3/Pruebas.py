'''
Created on 27/01/2015

@author: Daniel
@author: Gabriel
'''
import unittest
from Estacionamiento import Estacionamiento

class TestMarzullo(unittest.TestCase):
    
    def setUp(self):
        print('Preparando casos Marzulo')
        self.lista = []
        self.Esta = Estacionamiento()
        self.lista.append((10, 12))
        self.lista.append((8, 12))
        self.lista.append((10, 12))
        self.lista.append((10, 12))
        self.lista.append((10, 12))
        self.lista.append((7, 12))
        self.lista.append((6, 12))
        self.lista.append((9, 12))
        self.lista.append((10, 12))
        self.lista.append((10, 12))
        self.lista.append((10, 12))
        
        self.lista2 = []
        self.Esta2 = Estacionamiento()
        self.lista2.append((10, 12))
        self.lista2.append((6, 8))
        self.lista2.append((11,12))

    def tearDown(self):
        print('Limpiando casos Marzulo')

    def testReservacionInvalida_HoraIiguales1(self):
        estacio = Estacionamiento()        
        self.assertFalse(estacio.reservar(6,6))
        
    def testReservacionInvalida_EntradaMenor(self):  
        estacio=Estacionamiento()       
        self.assertFalse(estacio.reservar(5,12))
    
    def testReservacionInvalida_HoraEntradaMayor(self):
        estacio=Estacionamiento() 
        self.assertFalse(estacio.reservar(6,20))
        
    def test_CasoNormal(self):
        self.assertTrue(self.Esta2.anexar(self.lista2))
        
    def test_OnceCarrosMismoHorario(self):
        self.assertFalse(self.Esta.anexar(self.lista))

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestMarzullo)
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)