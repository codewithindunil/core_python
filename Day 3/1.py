class Dog:
    Info = {}  #commen for all objects
    # def __init__(self): #default constructor

    def __init__(self,name,age,weight):
        self.name=name#instance variable
        self.age=age
        self.weight=weight
    def printDetails(self):
        print(self.name)
        print(self.age)
        print(self.weight)
    def fillInfo(self,info):
        self.Info.clear()
        self.Info.update(info)
    def bark(self):
        for x in self.Info:
            print(x+" : "+str(self.Info[x]))
        print("Baww baww baww.....")

# bula  =Dog()
# bula.Info.setdefault("name","Bula")
# bula.Info.setdefault("age",5)
# bula.Info.setdefault("color","Brown")
# bula.bark()
# tommy=Dog()
# tommy.Info.setdefault("name","Tommy")
# tommy.Info.setdefault("age",4)
# tommy.Info.setdefault("kind","Labrador")
# tommy.bark()
tommy=Dog("Tommy",23,53.5)
# tommy.fillInfo({"name":"Tommy","weight":40})
# tommy.bark()
tommy.printDetails()