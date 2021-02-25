class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname + self.lastname)
p1=Person("Salman" ,"Rasheed")
p2=Person("Ali ","Haider")


