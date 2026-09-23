import numpy as np

n = np.array([10,20,30,40,50])
print(np.cumsum(n))  # cumsum = cumulative sum
print(np.cumprod(n))  # cumprod = cumulative multiplication


t = np.array([[1,2],[4,5]])
print(np.cumsum(t))
print(np.cumprod(t))


a = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(np.cumsum(a))
print(np.cumprod(a))
