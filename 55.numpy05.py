#identity matrix is used for co-relation
# in ML eye replace with t3.corr() method
import numpy as np

t3 = np.eye(3)
print(t3)


# why slicing or indexing in mumpy
# slicing in 1-D
# slicing in 2-D
a1 = np.array([1,2,3,4,5,6,7,8,9])
a2 = np.array([[1,2,3,4],[5,6,7,8]])
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(a3[0, 0, 2])  
print(a3[0, 1, 1])  
print(a3[0, 2, 0])  

print(a3[0, 1, :])
