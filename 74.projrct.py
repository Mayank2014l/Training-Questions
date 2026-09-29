import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import math

# ML implement -- Python

data = {
    "distance": [2, 4, 5, 7, 8, 10, 12, 14, 16],
    "fare": [60, 90, 110, 145, 165, 200, 235, 270, 305]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.corr())

# Numerical vs numerical -> scatter plot
sns.scatterplot(data=df, x="distance", y="fare")

plt.xlabel("Distance (KM)")
plt.ylabel("Fare")
plt.title("Distance vs Taxi Fare")

# Data divided into X and y
X = df[["distance"]]
y = df["fare"]

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
distance = float(input("Enter distance in KM: "))

fare = m * distance + c

if fare >= 0:
    print("Predicted Fare is:", round(fare, 2))
else:
    fare = 0
    print("Predicted Fare is:", round(fare, 2))

# Model comparison
compare_df = pd.DataFrame({
    "Actual X": X.values.flatten(),
    "Actual y": y.values,
    "Model Predicted Value": y_pred
})

print(compare_df)

# Regression line
plt.plot(
    compare_df["Actual X"],
    compare_df["Model Predicted Value"],
    color="g",
    marker="o",
    label="Best Line"
)

# Original data
plt.scatter(
    compare_df["Actual X"],
    compare_df["Actual y"],
    color="r",
    label="Original Data"
)

plt.title("Linear Regression Model")
plt.xlabel("Distance (KM)")
plt.ylabel("Fare")
plt.legend()

plt.show()

# MAE
MAE = (
    compare_df["Actual y"] -
    compare_df["Model Predicted Value"]
).abs().mean()

print("Mean Absolute Error:", round(MAE, 2))

# MSE
MSE = (
    (compare_df["Actual y"] -
     compare_df["Model Predicted Value"]) ** 2
).mean()

print("Mean Squared Error:", round(MSE, 2))

# RMSE
RMSE = math.sqrt(MSE)

print("Root Mean Squared Error:", round(RMSE, 2))

# R2 Score
model_score = model.score(X, y)

print("R² Score:", round(model_score, 4))