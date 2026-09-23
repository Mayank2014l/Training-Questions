import pandas as pd

# 1 Way 2D dataset
data = [
    [1, "david", "Developer",23000, "noida"],
    [2, "john", "Manager",30000, "delhi"],
    [3, "jane", "Analyst",25000, "mumbai"],
    [4, "rohit", "Tester",20000, "bangalore"]
]

df = pd.DataFrame(data,columns =["Id","Name","Post","Salary","City"])
print(df)


# 2nd ways 2D Dataset

emp = {
    "id":[1,2,3,4,5],
    "name":["ram","shyam","Mayank","Sahil","Abhinaw"],
    "post":["Developer","hr","Manager","clerk","programmer"],
    "Salary":[23000,34000,150000,20000,30000],
    "city":["noida","delhi","Gurgaon","faridabad","mohali"]
}
df = pd.DataFrame(emp)
print(df)

# get only name

print(df["name"])
# get top 2
print(df.head(2))
# get last 2 
print(df.tail(2))
#whose salary greater than 20000
print(df[df["Salary"]>20000])
# get salary b/w 35000 to 25000
print(df[(df["Salary"]>25000)&(df["Salary"]<35000)])
# how to get max,min salary
print(df["Salary"].max())
# how to get max,min salary
print(df["Salary"].min())
# how to get name,post and salary
print(df[["name","post","Salary"]])
# how to add new column ***
df["Experience"] = [2,3,4,5,6]
print(df)

