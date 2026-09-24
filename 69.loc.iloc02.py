import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Rahul", "Priya", "Aman", "Neha", "Arjun",
        "Rahul", "Simran", "Vikas", None, "Priya"
    ],
    "Post": [
        "Manager", "Developer", "Accountant", "HR", "Designer",
        "Developer", "Manager", None, "Accountant", "Developer"
    ],
    "Salary": [
        60000, 50000, 45000, 40000, None,
        50000, 65000, 42000, 45000, 50000
    ],
    "City": [
        "Delhi", "Mumbai", "Chandigarh", "Ludhiana", "Amritsar",
        "Mumbai", None, "Delhi", "Chandigarh", "Mumbai"
    ],
    "Age": [
        35, 28, 32, 30, 27,
        None, 38, 29, 32, 28
    ]
}

df = pd.DataFrame(data)

# Very important concept: Data Preprocessing

# EDA: Shape and Columns
print(df.shape)
print(df.columns)

# Information about DataFrame
df.info()

# Check null values
print(df.isnull())

# Check non-null values
print(df.notnull())

# Count null values in each column
print(df.isnull().sum())

# Count non-null values in each column
print(df.count())

# Fill missing values with 0
df = df.fillna(0)
print(df)

# Drop rows containing null values
df1 = df.dropna()
print(df1)