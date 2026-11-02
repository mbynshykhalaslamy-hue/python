class rectangle:
    def __init__(self):

        self.width=float(input("عرض را درج نماييد"))
        self.lagth=float(input("طول را درج نماييد")) 


    def masahat(self):
        
        s=self.width*self.lagth

        return s
    
    def mohet(self):
        
        p=(self.width+self.lagth)*2
        
        return p
    
rect1=rectangle()
print(rect1.masahat())
print(rect1.mohet())
