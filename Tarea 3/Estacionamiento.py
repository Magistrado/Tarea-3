'''
Created on 27/01/2015

@author: Daniel
@author: Gabriel
'''
from Tuplas import Tuplas
from Reserva import Reserva
import functools

class Estacionamiento:
    #Atribtuos Marzullo
        
    # Formato de la hora: hh:mm en 24 horas    
    tablasTuplas=[]
    reservasAdmitidas=[]
    capacidad = 10

    def reservar(self, horaEntrada, horaSalida):
        if horaEntrada<6 or horaEntrada>18:
            print("Horas introducidas invalidas")
            return False
        
        if  horaSalida>18 or horaSalida<6:
            print("Horas introducidas invalidas")
            return False
       
        if horaEntrada>=horaSalida:
            print("La hora entrada debe ser menor a la salida")
            return False       
        
        #Convertir en tupla para uso del algoritmo de Marzullo
        tupla1 = Tuplas(horaEntrada,-1)
        self.tablasTuplas.append(tupla1)        
        tupla2 = Tuplas(horaSalida,1)
        self.tablasTuplas.append(tupla2)        
        
        return self.algoritmoMarzullo()
        
    def algoritmoMarzullo(self):  
        best = 0
        cnt = 0
        beststart = 0
        bestend = 0
        self.tablasTuplas.sort(key=functools.cmp_to_key(self.compararTuplas))
        i = 0
        for tupla in self.tablasTuplas:
            i += 1
            cnt -= tupla.obtType()
            if best < cnt:
                best=cnt
                beststart = tupla.obtOffset()
                if i < len(self.tablasTuplas) -1 :
                    bestend = self.tablasTuplas[i+1].obtOffset()           
        if best <= self.capacidad:
            self.reservasAdmitidas.append(Reserva(beststart, bestend))
            print('Reservacion concretada con exito.')
            return True
        else:
            print('Capacidad excedida.')
            return False
        
    def compararTuplas(self,tupla1, tupla2):
        return tupla1.offset - tupla2.offset
    
    def anexar(self, listacasos):
        for caso in listacasos:
            if not self.reservar(caso[0], caso[1]):
                return False
        return True