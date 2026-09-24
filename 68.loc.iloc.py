import pandas as pd
import numpy as np

data = {
    "product_id": [101,102,103,104,105,106,107,108,109,110],
    "name": [
        "Laptop", "Mobile", "Keyboard", "Mouse", "Monitor",
        "Headphone", "Printer", "Tablet", "Camera", "Speaker"
    ],
    "price": [
        60000, 25000, 1500, 800, 12000,
        3000, 15000, 20000, 18000, 5000
    ],
    "quantity": [
        1, 2, 3, 5, 1,
        2, 1, 1, 2, 1
    ]
}

df = pd.DataFrame(data)

print(df.loc[2, "name"]) # Get particular cell

print(df.loc[:, "name"]) # Get particular column

print(df.loc[:, ["name", "price"]]) # Get multiple columns

print(df.loc[[1, 3, 5]]) # Get multiple rows

print(df.loc[df["price"] > 10000]) # Get rows where price is greater than 10000

print(df.loc[df["quantity"] > 1]) # Get rows where quantity is greater than 1

print(df.loc[df["price"] < 5000]) # Get rows where price is less than 5000

print(df.loc[(df["price"] > 10000) & (df["quantity"] == 5)]) # Get products where price is greater than 10000 and quantity is 5

print(df.iloc[2,3])

# get multiple records/rows using iloc function
print(df.iloc[[1,2,3,4]])

# get first 3 records
print(df.iloc[0:3])

# get last record
print(df.iloc[:,-1])

# get first 3 rows and 2 columns
print(df.iloc[0:3,0:2])