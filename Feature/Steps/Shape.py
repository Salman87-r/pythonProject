class shape:
    def __init__(self,number):
        self.number=number
    def calculteperimater(self):
        result=sum(self.number)
        return  result
    def display_info(self):
        print("I am in base  class")
class triangle(shape):
    def display_info(self):
        print("I am in triangle class")
class square(shape):
    def display_info(self):
        print("I am in square class")

t1=triangle([3,5,6])
print(t1.calculteperimater())
t1.display_info()
t2=square([4,6])
print(t2.calculteperimater())
t2.display_info()