import pandas as pd
import numpy as np

s1 = pd.Series()
print(s1)
s2 = np.array([1,2,3,4,5])
s3 = pd.Series(s2)
print(s3)
s4 = pd.Series([11,12,13,14])
print(s4)


#Customize indexing are very important in ML
s5 = pd.Series(["aman","sonu","rohit","monu"],index=["A","B","C","D"])
print(s5)


s6 = pd.Series([10,20,30,40,50,60])
print(s6.index)
print(s6.shape)  # for dimension
print(s6.size)
print(s6.values)
print(s6.dtype)  # type of data ML 