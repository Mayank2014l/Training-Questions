import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# ==================== DATA ====================

data = {
    "study-hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)


# ==================== DATA INFORMATION ====================

print(df)

print("\nShape:")
print(df.shape)

print("\nCorrelation:")
print(df.corr())


# ==================== GRAPH ====================

plt.figure(figsize=(8, 5))

plt.plot(
    df["study-hours"],
    df["marks"],
    color="red",
    linestyle="--"
)

sns.scatterplot(
    data=df,
    x="study-hours",
    y="marks"
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()


# ==================== X AND Y ====================

X = df[["study-hours"]]
Y = df["marks"]


# ==================== MODEL ====================

model = LinearRegression()

print("\nModel:")
print(model)


# ==================== TRAINING ====================

model.fit(X, Y)

print("\nModel trained successfully!")


# ==================== PREDICTION ====================

prediction = model.predict([[10]])

print(
    "\nPredicted marks for 10 study hours:",
    round(prediction[0], 2)
)


# ==================== COEFFICIENT AND INTERCEPT ====================

intercept = model.intercept_
coefficient = model.coef_[0]

print("\nIntercept:", round(intercept, 2))
print("Coefficient:", round(coefficient, 2))


# ==================== FORMULA ====================

print(
    "\nLinear Regression Equation:"
)

print(
    "Marks =",
    round(coefficient, 2),
    "* Study Hours +",
    round(intercept, 2)
)


# ==================== USER INPUT ====================

study_hours = float(
    input("\nEnter study hours: ")
)

predicted_marks = (
    coefficient * study_hours
    + intercept
)

print(
    "Predicted marks for",
    study_hours,
    "study hours:",
    round(predicted_marks, 2)
)