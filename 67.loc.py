import pandas as pd
import numpy as np

data = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "name": [
        "Rahul", "Aman", "Priya", "Neha", "Arjun",
        "Karan", "Sneha", "Vikas", "Riya", "Aditya"
    ],
    "post": [
        "Developer", "Data Analyst", "Manager", "Tester", "Developer",
        "HR", "Data Scientist", "Designer", "Developer", "Manager"
    ],
    "salary": [
        60000, 55000, 90000, 25000, 70000,
        50000, 95000, 35000, 75000, 85000
    ],
    "city": [
        "Delhi", "Chandigarh", "Mumbai", "Pune", "Bangalore",
        "Delhi", "Hyderabad", "Chandigarh", "Noida", "Mumbai"
    ],
    
}

df = pd.DataFrame(data)
#print(df)

print(df.loc[3]) # get rown number 3 not index

print(df.loc[2,"city"]) # get city of 2nd row

# get particular column
print(df.loc[:,"name"])

# get multiple column
print(df.loc[:,["name","salary"]])

# get multiple rows
#print(df.loc[:,[1,2,4]])

print(df.loc[df["salary"]>30000])

print(df.loc[df["city"] == "Delhi"])

print(df.loc[(df["city"] == "Delhi") & (df["salary"] > 30000)])