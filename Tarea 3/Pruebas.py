'''
Created on 27/01/2015

@author: Daniel
@author: Gabriel
'''
import unittest
from Estacionamiento import Estacionamiento

class TestMarzullo(unittest.TestCase):
    
    def setUp(self):
        print('\nPreparando casos Marzulo')
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
        self.lista.append((7, 12))
        
        self.lista2 = []
        self.lista2.append((10, 12))
        self.lista2.append((6, 8))
        self.lista2.append((11,12))
        
        self.lista3 = []
        self.lista3.append((10, 12))
        self.lista3.append((8, 12))
        self.lista3.append((10, 12))
        self.lista3.append((10, 12))
        self.lista3.append((10, 12))
        self.lista3.append((7, 12))
        self.lista3.append((6, 12))
        self.lista3.append((9, 12))
        self.lista3.append((10, 12))
        self.lista3.append((10, 12))

    def tearDown(self):
        print('Limpiando casos Marzulo\n')

    def testReservacionInvalida_HoraIiguales1(self):
        estacio = Estacionamiento()        
        self.assertFalse(estacio.reservar(6,6))
        
    def testReservacionInvalida_EntradaMenor(self):  
        estacio=Estacionamiento()       
        self.assertFalse(estacio.reservar(5,12))
    
    def testReservacionInvalida_HoraEntradaMayor(self):
        estacio=Estacionamiento() 
        self.assertFalse(estacio.reservar(6,20))
        
    def testCarrosMismoHorario(self):
        self.assertTrue(self.Esta.anexar(self.lista3))
        
    def testOnceCarrosMismoHorario(self):
        self.assertFalse(self.Esta.anexar(self.lista))

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestMarzullo))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)