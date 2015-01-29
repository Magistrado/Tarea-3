'''
Created on 27/01/2015

@author: Daniel
'''
from Reserva import Reserva
from Tuplas import Tuplas
import functools

class Estacionamiento(object):
    puestos =[]
    tablasTuplas=[]
    #Atribtuos Marzullo
        
    # Formato de la hora: hh:mm en 24 horas    
    def reservar(self, horaEntrada, horaSalida):
        if horaEntrada<6 and horaEntrada>18:
            return "Horas introducidas invalidas"  
        
        if  horaSalida>18 and horaSalida<6:
            return "Horas introducidas invalidas" 
       
        if horaEntrada>=horaSalida:
            return "La hora entrada debe ser menor a la salida"
        
        fuente=0
        reservaEntrante=Reserva(fuente,horaEntrada,horaSalida)
        fuente+=1
        self.puestos.append(reservaEntrante)
        self.algoritmoMarzullo()
        
     
        
    def algoritmoMarzullo(self):  
        best=0
        cnt=0
        beststart=0
        bestend=0
        iden = ''
        for reserva in self.puestos:
            tupla1=Tuplas(reserva.obtId(),reserva.obtInicio(),-1)
            self.tablasTuplas.append(tupla1)
            tupla2=Tuplas(reserva.obtId(),reserva.obtFinal(),1)
            self.tablasTuplas.append(tupla2)
            self.puestos.remove(reserva)
        
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
                    iden = tupla.obtId() + ', ' + self.tablasTuplas[i+1].obtId()
        if best <= 10:            
            resultado = Reserva(iden, beststart, bestend)
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