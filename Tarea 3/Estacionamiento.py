'''
Created on 27/01/2015

@author: Daniel
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
        if horaEntrada<6 and horaEntrada>18:
            return "Horas introducidas invalidas"  
        
        if  horaSalida>18 and horaSalida<6:
            return "Horas introducidas invalidas" 
       
        if horaEntrada>=horaSalida:
            return "La hora entrada debe ser menor a la salida"        
        
        print("\nRESERVA EN PROGRESO")
        #Convertir en tupla para uso del algoritmo de Marzullo
        tupla1 = Tuplas(horaEntrada,-1)
        self.tablasTuplas.append(tupla1)        
        tupla2 = Tuplas(horaSalida,1)
        self.tablasTuplas.append(tupla2)        
        
        self.algoritmoMarzullo()
        
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
        
Esta=Estacionamiento()    
Esta.reservar(8,12)
Esta.reservar(11,13)
Esta.reservar(10,12)
   

'''
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
Esta=Estacionamiento(10)
Esta.anexarCasos(lista)
print(lista)
'''
Esta.reservar(10,12)
Esta.reservar(11,13)
Esta.reservar(8,12)
Esta.reservar(6,12)
'''    
Esta.reservar(10,12)
Esta.reservar(11,13)
Esta.reservar(8,12)
'''
