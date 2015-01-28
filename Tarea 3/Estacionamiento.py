'''
Created on 27/01/2015

@author: Daniel
'''
from Reserva import Reserva
from Tuplas import Tuplas

class Estacionamiento(object):
    puestos =[]
    tablasTuplas=[]
    #Atribtuos Marzullo
    

    #def __init__(self, capacidad,intervalo_trabajo):
        #puestos= [[0 for x in range(capacidad)] for x in range(intervalo_trabajo*2)]
       # puestos= [range(intervalo_trabajo*2) for i in range(capacidad)]
        
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
        #print(reservaEntrante.__str__())
        fuente+=1
        self.puestos.append(reservaEntrante)
        print(self.puestos)
        #reservaFactible=
        self.algoritmoMarzullo()
        
     
        
    def algoritmoMarzullo(self):  
        best=0
        cnt=0
        beststart=0
        bestend=0
        for reserva in self.puestos:
            tupla=Tuplas(reserva.obtId(),reserva.obtInicio(),-1)
            print(tupla)
            self.tablasTuplas.append(tupla)
            tupla=Tuplas(reserva.obtId(),reserva.obtFinal(),+1)
            print(tupla.__str__())
            self.tablasTuplas.append(tupla)
        
        self.tablasTuplas.sort(key=)
            
        
        
Esta=Estacionamiento()    
Esta.reservar(6, 8)
Esta.reservar(6, 10)