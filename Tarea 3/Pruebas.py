'''
Created on 27/01/2015

@author: Daniel
'''
import unittest
from Estacionamiento import Estacionamiento



class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReservacionInvalida_HoraIiguales1(self):
        estacio=Estacionamiento()        
        self.assertEqual(estacio.reservar(6,6),"Horas introducidas invalidas")
        
    def testReservacionInvalida_HoraIiguales2(self):  
        estacio=Estacionamiento()       
        self.assertEqual(estacio.reservar(18,18),"Horas introducidas invalidas")
    
    def testReservacionInvalida_HoraEntradaMayorHoraSalida(self):
        estacio=Estacionamiento() 
        self.asserEqual(estacio.reservar(18,6), "La hora entrada debe ser menor a la salida")
                

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()