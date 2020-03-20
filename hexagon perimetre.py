class Hexagon():
    def __init__(self, a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f

    def perimetr(self):
        return self.a+self.b+self.c+self.d+self.e+self.f

    

hexagon1=Hexagon(4,5,6,7,8,9)
print(hexagon1.perimetr())
