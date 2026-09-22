import numpy as np
n1 = np.array([1,2,3,4,5])
print(n1)
print(n1.size)
print(type(n1))


n3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(n3)
print(n3.size)
print(type(n3))
print(n3.ndim)
# in case you use 3-D array they must be converted into 2-D 
# the model trained

n4 = np.array([[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]])
print(n4)
print(n4.size)
print(type(n4))
print(n4.ndim)

n5 = np.array(list(map(int,input("Enter elements: ").split())))
print(n5)


