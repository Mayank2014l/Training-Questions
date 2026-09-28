import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# ML implement -- Python

data = {
    "study-hour": [2, 4, 5, 7, 8, 10, 11, 13, 15],
    "marks": [28, 35, 42, 50, 58, 66, 72, 81, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.corr())

plt.plot(df["study-hour"], df["marks"], color="r", linestyle="--")

# Numerical vs numerical -> scatter plot
sns.scatterplot(data=df, x="study-hour", y="marks")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

# Data divided into X and y
X = df[["study-hour"]]
y = df["marks"]

# Model build
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
Study_hours = float(input("Enter study hour: "))

marks = m * Study_hours + c

# Keep marks between 0 and 100
if 0 <= marks <= 100:
    print("Predicted value is:", round(marks, 2))

elif marks < 0:
    marks = 0
    print("Predicted value is:", round(marks, 2))

else:
    marks = 100
    print("Predicted value is:", round(marks, 2))

# Model comparison
compare_df = pd.DataFrame({
    "Actual X": X.values.flatten(),
    "Actual y": y.values,
    "Model Predicted Value": y_pred
})

print(compare_df)

plt.show()