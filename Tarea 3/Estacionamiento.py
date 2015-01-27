'''
Created on 27/01/2015

@author: Daniel
'''

class Estacionamiento(object):
    puestos =[]

    #def __init__(self, capacidad):
        #puestos= [[0 for x in range(5)] for x in range(5)]
        
    # Formato de la hora: hh:mm en 24 horas    
    def reservar(self, horaEntrada, horaSalida):
        if horaEntrada>=6 and horaSalida>6 and horaEntrada<18 and horaSalida<=18:
            return "Horas introducidas invalidas" 
        if horaEntrada>horaSalida:
            return "La hora entrada debe ser menor a la salida"
        
        
        
        
        