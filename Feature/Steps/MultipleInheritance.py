class person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
class dancer:
  def __init__(self,style):
      self.style=style

class boy(person, dancer):
    def __init__(self,age,name,style):
        dancer.__init__(self,style)
        person.__init__(self,age,name)
b1=boy(12,"Salman","HipHop")

print(b1.style)
print(b1.age)
