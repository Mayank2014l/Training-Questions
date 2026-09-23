import numpy as np

player = np.array(["Rohit", "Virat", "Gill", "Hardik", "Pant"])
runs = np.array([85, 102, 67, 45, 78])
balls = np.array([62, 110, 51, 32, 55])

score = []
result = []

for r, b in zip(runs, balls):

    if r >= 100:
        score.append("Century")
        result.append(r)

    elif r >= 50:
        score.append("Half Century")
        result.append(r)

    else:
        score.append("Low Score")
        result.append(r)

score = np.array(score)
result = np.array(result)

strike_rate = runs / balls * 100

print("\n------ CRICKET SCORE -------")
print("Players       :", player)
print("Runs          :", runs)
print("Balls         :", balls)
print("Strike Rate   :", np.round(strike_rate, 2))
print("Performance   :", score)