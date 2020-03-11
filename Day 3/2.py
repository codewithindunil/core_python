class Student:
    collage = "SLIIT"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printDetails(self):
        print("Name is " + str(self.name))
        print("Age is " + str(self.age))
        print("Gender is " + str(self.gender))
    def trstSelf(self):
        self.marks=52


print(Student.collage)
s1 = Student("Kanishka", 52, "Male")
s2 = Student("Tharindu", 24, "Male")
s1.printDetails()
s2.printDetails()
s1.trstSelf()
print(s1.marks)
