class Complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img
    def add(self, num):
        real=self.real + num.real
        img=self.img+num.img
        result=Complex(real,img)
        return  result
n1=Complex(5,6)
n2=Complex(-4,4)
res=n1.add(n2)
print(res.real)
print(res.img)