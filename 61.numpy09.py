# axis=0 means up and down
# axis=1 mens left to right

import numpy as np

n = np.array([
    [10,20,30],
    [40,50,60]
])
print(n)
print(np.sum(n,axis=0))
print(np.sum(n,axis=1))


t = np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]])
print(t)
print(np.sum(t,axis=0))
print(np.sum(t,axis=1))