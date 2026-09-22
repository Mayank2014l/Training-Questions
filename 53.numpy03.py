import numpy as np

row = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
t = []

for i in range (row):
    v = list(map(int,input().split()))
    t.append(v)
n7 = np.array(t)
print(n7)