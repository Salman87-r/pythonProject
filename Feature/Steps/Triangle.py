class triangle:
    def __init__(self ,a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def calcupara(self):
        add=self.a +self.b +self.c
        result=add/2
        return  result

t1=triangle(3,2,5)
print(t1.calcupara())