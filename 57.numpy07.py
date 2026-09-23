import numpy as np

#next is age and salary (inc or dec)
# in product, if purchase 10000 then free delievery
# in product if purchase 5000 then 5% discount
# is used for (inc or dec)
a = np.array([1,2,3,4,5,6,7,8,9])
x=a+2
y=a*2
print(x)
print(y)

#*****************************************************#
a1 = np.array([[1,2,3,4],[5,6,7,8]])
a2 = np.array([11,12,13,14])
z1 = a1+a2
z2 = a1*a2
z3 = a1-a2
z4 = a1/a2
z5 = a1%a2
z6 = a1**a2
z7 = a1//a2
z8 = a1@a2

print(z1)
print(z2)
print(z3)
print(z4)
print(z5)
print(z6)
print(z7)
print(z8)