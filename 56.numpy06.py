import numpy as np

x = np.arange(1,9)
y = x.reshape(2,2,2)
print(y)
print(y.ndim)