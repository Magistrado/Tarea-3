'''
Created on 27/01/2015

@author: Daniel
'''
from Tuplas import Tuplas
import functools

class Estacionamiento:
    tablasTuplas=[]
    reservasAdmitidas=[]
    capacidad=0
    
    def __init__(self,capacidad):
        self.capacidad=capacidad
         
    def reservar(self, horaEntrada, horaSalida):
        if horaEntrada<6 and horaEntrada>18:
            return "Horas introducidas invalidas"  
        
        if  horaSalida>18 and horaSalida<6:
            return "Horas introducidas invalidas" 
       
        if horaEntrada>=horaSalida:
            return "La hora entrada debe ser menor a la salida"        
        
        
        print("\nRESERVA EN PROGRESO")
        #Convertir en tupla para uso del algoritmo de Marzullo
        tupla1=Tuplas(horaEntrada,-1)
        self.tablasTuplas.append(tupla1)        
        tupla2=Tuplas(horaSalida,1)
        self.tablasTuplas.append(tupla2)        
        reservaFactible=self.algoritmoMarzullo() 
        print(reservaFactible)
        
        if self.capacidad>reservaFactible[0]:
            if (horaEntrada==reservaFactible[1] 
                and horaSalida==reservaFactible[2] 
                    and len(self.reservasAdmitidas)>0):                
                return False
            else:
                self.reservasAdmitidas.append([horaEntrada,horaSalida])
                print("Reservas Admitidas: %s " % (self.reservasAdmitidas))
                return True
        else:
            return False
    
    
        
    def algoritmoMarzullo(self):  
        best=0
        cnt=0
        beststart=0
        bestend=0
        i=0        

        self.tablasTuplas.sort(key=functools.cmp_to_key(self.compararTuplas))
        print(self.tablasTuplas)
        for tupla in self.tablasTuplas:
            cnt-= tupla.obtType()
            if best<cnt:
                best=cnt
                beststart = tupla.obtOffset()
                if (i<len(self.tablasTuplas)-1):
                    bestend=self.tablasTuplas[i+1]
                    bestend=bestend.obtOffset()
            i+=1
            '''
            Caso extremo del algoritmo. Probar
            if best==cnt:
                return [best,beststart,bestend]
            '''
        #Mejor repuesta: 
        #Best=capacidadEstacionamiento
        #Beststart y bestend=Intervalo de mayor ocupacion     
        return [best,beststart,bestend]

    def anexarCasos(self,lista):
        self.tablasTuplas.extend(lista)
        
    def compararTuplas(self,tupla1, tupla2):
        return tupla1.offset - tupla2.offset   
   

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
Esta=Estacionamiento(10)
print(Esta.reservar(10,12))
print(Esta.reservar(11,13))
print(Esta.reservar(8,12))
print(Esta.reservar(6,12))
'''    
Esta.reservar(10,12)
Esta.reservar(11,13)
Esta.reservar(8,12)
'''