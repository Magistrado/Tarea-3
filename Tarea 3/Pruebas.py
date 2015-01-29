'''
Created on 27/01/2015

@author: Daniel
'''
import unittest
from Estacionamiento import Estacionamiento
from Tuplas import Tuplas

class Test(unittest.TestSuite):
    
    class Test_EntradasReservacion(unittest.TestCase):
        
        def setUp(self):
            pass
    
        def tearDown(self):
            pass
    
        def testReservacionInvalida_HoraIiguales1(self):
            estacio=Estacionamiento()        
            self.assertEqual(estacio.reservar(6,6),
                             "Horas introducidas invalidas")
            
        def testReservacionInvalida_HoraIiguales2(self):  
            estacio=Estacionamiento()       
            self.assertEqual(estacio.reservar(18,18),
                             "Horas introducidas invalidas")
        
        def testReservacionInvalida_HoraEntradaMayorHoraSalida(self):
            estacio=Estacionamiento() 
            self.assertEqual(estacio.reservar(18,6), 
                             "La hora entrada debe ser menor a la salida")
     

    class TestAlgoritmoMarzullo(unittest.TestCase): 
    
        def Test_CasoPequeño(self):
            lista=[]
            tupla1=Tuplas(10,-1)
            lista.append(tupla1) 
            tupla1=Tuplas(12,1)
            lista.append(tupla1)
            tupla1=Tuplas(11,-1)
            lista.append(tupla1)
            tupla1=Tuplas(13,1)
            lista.append(tupla1)
            tupla1=Tuplas(8,-1)
            lista.append(tupla1)
            tupla1=Tuplas(12,1)
            lista.append(tupla1)
            Esta=Estacionamiento()
            Esta.anexar(lista)
            TuplaSol=Tuplas(11,12)
            tuplaResul=Esta.algoritmoMarzullo()
            self.AssertEqual(tuplaResul,TuplaSol)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()