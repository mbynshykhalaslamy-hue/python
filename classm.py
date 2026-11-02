class moraba:

    def __init__(self):
        
        self.width=float(input("عرض را درج نماييد"))


    def masahat(self):
        
        m=self.width*self.width

        print(f"مساحت مربع برابر است با {m}")

    def mohet(self):

        o=self.width*4
        print(f"محيط مربع برابر است با {o}")
        

mor1=moraba()
print(mor1.masahat())
print(mor1.mohet())
