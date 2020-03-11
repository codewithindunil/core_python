class Shape:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def perimetert(self):
        P1 = 2 * (self.length + self.width)
        P2 = 2 * 3.14 * self.radius
        return P1, P2

    def area(self):
        A1 =( self.length * self.width)
        A2 = self.radius * self.radius * 3.14
        return A1,A2


class Rectangle(Shape):
    def print(self):
        print(self.perimetert())
        print(self.area())


class Square(Rectangle):
    pass


class Circle(Shape):
    def print(self):
        self.perimetert()
        self.area()


x = Rectangle(0,0 , 10)
x.print()
