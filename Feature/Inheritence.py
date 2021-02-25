class Student:
    def check_pass_Fail(self):
        if self.marks>= 40:
            return True
        else:
            return False
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

S1= Student("Hamza",30)
print(S1.check_pass_Fail())
print(S1.name)
