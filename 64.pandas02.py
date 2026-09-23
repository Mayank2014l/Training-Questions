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
    "age": [
        25, 28, 35, 24, 30,
        27, 32, 29, 26, 38
    ]
}

df = pd.DataFrame(data)
print(df)

# add column bonus salary >= 40000 5%
df["bonus"] = np.where(df["salary"] > 40000, df["salary"] * 0.05, 0)  # lamda x: Ek value lo aur uspar calculation karo.
# add column hra Salary 10%
df["hra"] = df["salary"] * 0.10
# add column da 5%
df["da"] = df["salary"] * 0.05
# add column calculate Gross Salary
df["gross_salary"] = df["salary"] + df["bonus"] + df["hra"] + df["da"]
#add column calculate Net Salary
df["net_salary"] = df["gross_salary"]


print(df)