from Person import Person


class Student(Person):
    def __init__(self,fname,lname,year):
       super().__init__(fname,lname)
       self.graduationyear = year
p3=Student("Salman ","Rasheed",1990)
p3.printname()
print(p3.graduationyear)
