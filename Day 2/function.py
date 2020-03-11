# def add(x,y):
#     sum=x+y
#     return sum
# print("Answer = "+str(add(11,12)))

# def add(x,y):
#     sum=x+y
#     print("Answer = "+str(sum))
#
# add(12,13)
# def add():
#     x=52
#     y=2
#     sum=x+y
#     return sum
#
# print("Answer = "+str(add()))

# def add():
#     x = 54
#     y = 20
#
#     sum=x+y
#     print("Answer = "+str(sum))
# add()

# def getData():
#     name="kanishka"
#     age=29
#     gender="male"
#     return name,age,gender
# answer=getData()
# print("name - "+answer[0])
#
# def printData(name,age):
#     print("Name - "+name)
#     print("Age - "+str(age))
#
# printData("Nimal",45)

# def printData(*data):
#     for x in data:
#         print(x)
# list0=[]
#
# for i in range(1,11):
#    list0.append(i)
#
# printData(list0)
# x=lambda a,b:(a+b)/2
# print(x(12,20))
def testLambda(x,y):
    for i in range(1,x+1):
        print(y(i))

p= lambda q: q**2
testLambda(10,p)

def testLambda(x,y):
    for i in range(1,x+1):
        print(y(i))

p= lambda q: q**3
testLambda(10,p)