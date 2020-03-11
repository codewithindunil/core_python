import numpy as np
# z=np.array([[0,0],[0,0],[0,0],[0,0],[0,0]])
z=np.arange(10).reshape(5,2)
for i in range(0,5):
        z[i][0]=float(input("Enter Waight - "))
        z[i][1]=float(input("Enter Hight - "))
print(z)
print(type(z))
