class Person:  # base class
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def printPerson(self):
        print("Name - " + self.name)
        print("Gender - " + self.gender)


class Employee(Person):
    def printEmployee(self):
        self.printPerson()
        print("Sallery - " + str(self.sallery))
        print("Job - " + self.job)

    def __init__(self, name, gender, sallery, job):
        self.name = name
        self.gender = gender
        self.sallery = sallery
        self.job = job


e1 = Employee("Kanishka", "Male", 10000, "Eng")
e1.printEmployee()
