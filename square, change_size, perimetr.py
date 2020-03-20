class Square():
    def __init__(self, w,l):
        self.w=w
        self.l=l

    def change_size(self, x):

        self.w=self.w+x
        self.l=self.l+x
        
    

    def perimetr(self):
        return self.w*self.l
       


square= Square(10,15)
square.change_size(10)
print(square.l)
print(square.w)
print(square.perimetr())


