import numpy as np

# a = np.arange(0.2, 7.2)
# print(a)
# print(type(a))
# print(np.arange(0.5, 10.4, 0.8, int))
# #print(np.linspace(1, 100))  # default 50
# print(np.linspace(1,10,127,retstep=True))
#
# ndarray,step=np.linspace(1,10,100,retstep=True)
# print(ndarray)
# print(step)
# x=np.array(34)#zero dimentional
# print(np.ndim(x))
# a=np.array([1,2,3,4,5])
# print(a)
# print(np.ndim(a))
# print(a.dtype)
#
# b=np.array([1.1,2.2,3.3])
# print(b.dtype)

a=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
b=np.array([[[1,2],[2,3]],
            [[1,2],[2,3]],
            [[1,2],[2,3]]])
print(np.ndim(a))
print(a.dtype)
print(np.shape(a))
# print(np.ndim(b))
# print(b.dtype)
# print(b)
r,c=np.shape(a)
print(r)
print(c)
print(np.shape(b))
a.shape=(6,2)

