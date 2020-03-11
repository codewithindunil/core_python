class A:
    def sing(self):
        print("blh blah")
class B:
    def cry(self):
        print("errrrrrrrrr")
class C(A,B):
    def singAndCry(self):
        self.sing()
        self.cry()
c1=C()
c1.singAndCry()