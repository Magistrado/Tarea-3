class Tuplas():
    offset=0
    type=0
    iden=0
    
    def __init__(self,iden,ini,fin):
        self.offset=ini
        self.type=fin
        self.iden=iden
    
    def obtId(self):
        return self.iden
    
    def obtOffset(self):
        return self.offset
    
    def obtType(self):
        return self.type
    
    def __str__(self):
        return '['+str(self.offset)+','+str(self.type)+']'
    
