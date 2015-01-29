class Tuplas():
    offset=0
    type=0
    
    def __init__(self,offset,ty):
        self.offset=offset
        self.type=ty

    def obtOffset(self):
        return self.offset
    
    def obtType(self):
        return self.type
    
    def __str__(self):
        return '['+str(self.offset)+','+str(self.type)+']'
    
    def __repr__(self):
        return '['+str(self.offset)+','+str(self.type)+']'
