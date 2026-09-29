#Linear Regression 2nd Project
#emp_exp=[1-----------------20]
#emp_salary=[10000,---------------------]
#final prediction ?


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data = {
    "emp_exp": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20],

    "emp_salary": [
        25000, 28000, 32000, 35000, 39000,
        42000, 46000, 49000, 53000, 56000,
        60000, 63000, 67000, 70000, 74000,
        77000, 81000, 84000, 88000, 92000
    ]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.corr())

sns.scatterplot(data=df, x="emp_exp", y="emp_salary")

plt.xlabel("Employee Experience")
plt.ylabel("Employee Salary")
plt.title("Employee Experience vs Salary")

X = df[["emp_exp"]]
y = df["emp_salary"]
model = LinearRegression()

# Model trained
model.fit(X, y)

# y = mx + c
m = model.coef_[0]
print("m =", round(m, 2))

c = model.intercept_
print("c =", round(c, 2))

# Prediction for complete dataset
y_pred = model.predict(X)
print("Predicted values:", y_pred)

# User input
experience = float(input("Enter employee experience: "))

# Final prediction
salary = m * experience + c
print("Predicted Salary:", round(salary, 2))

# Model comparison
compare_df = pd.DataFrame({
    "Actual Experience": X.values.flatten(),
    "Actual Salary": y.values,
    "Model Predicted Salary": y_pred
})
print(compare_df)

plt.plot(
    compare_df["Actual Experience"],
    compare_df["Model Predicted Salary"],
    color="g",
    marker="o",
    label="Best Line"
)

plt.scatter(
    compare_df["Actual Experience"],
    compare_df["Actual Salary"],
    color="r",
    label="Original Data"
)

plt.title("Linear Regression Model")
plt.xlabel("Employee Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

MAE = (
    compare_df["Actual Salary"] -
    compare_df["Model Predicted Salary"]
).abs().mean()
print("Mean Absolute Error:", round(MAE, 2))

MSE = (
    (compare_df["Actual Salary"] -
     compare_df["Model Predicted Salary"]) ** 2
).mean()
print("Mean Squared Error:", round(MSE, 2))

import math

RMSE = math.sqrt(MSE)
print("Root Mean Squared Error:", round(RMSE, 2))

model_Score = model.score(X, y)
print("After Training Model Score is:", model_Score)