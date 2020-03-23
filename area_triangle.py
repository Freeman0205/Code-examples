class Triangle ():

    def __init__(self, a,h):
        self.asn=a
        self.vis=h
        self.area_triangle=1/2*a*h

    
triangle1=Triangle(7,10)
print(triangle1.area_triangle)
