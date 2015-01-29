class Reserva():
    inicio=0
    final=0
    iden=0
    
    def __init__(self,iden,ini,fin):
        self.inicio=ini
        self.final=fin
        self.iden=iden
    
    def obtId(self):
        return str(self.iden)
    
    def obtInicio(self):
        return self.inicio
    
    def obtFinal(self):
        return self.final
    
    def __str__(self):
        return '['+str(self.inicio)+','+str(self.final)+']'