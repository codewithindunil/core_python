class Polygon:
    def __init__(self, sidesCount):
        self.sidesCount = sidesCount
        self.sides = [0 for i in range(sidesCount)]

    def inputSidesLength(self):
        self.sides = [float(input("Enter sides l -")) for i in self.sides]

    def showSides(self):
        for i in range(self.sidesCount): print("side", i + 1, "is", self.sides[i])
    def area(self):
        a,b,c=self.sides
        # A = (0.5)*(a)*(((b-b)-(a/2*a/2))**0.5)

        y=(a+b+c)/2
        A= (y*(y-a)*(y-b)*(y-c))**0.5
        print("Area of Triangle - ",A)

class Triangle(Polygon):
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(3)


t1 = Triangle()
# t1.inputSidesLength()
# t1.showSides()
# t1.area()
# # p1=Polygon(3)
# print(p1.sides)
# p1.inputSidesLength()
# print(p1.sides)
print(isinstance(t1,Triangle))
print(isinstance(t1,Polygon))
print(issubclass(Triangle,Polygon))
print(issubclass(Polygon,object))
