# 1) ARRAY INFORMATION

import numpy as np

print("\n" + "="*50)
print("1) ARRAY INFORMATION")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])

print("Number of elements:", sales.size)
print("Dimensions:", sales.ndim)
print("Type:", sales.dtype)
print("Shape:", sales.shape)


# 2) TOTAL SALES

print("\n" + "="*50)
print("2) TOTAL SALES")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])
total = np.sum(sales)

print("Total sales:", total)


# 3) AVERAGE SALES

print("\n" + "="*50)
print("3) AVERAGE SALES")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])
average = np.mean(sales)

print("Average sales:", average)


# 4) MAXIMUM, MINIMUM, MAXIMUM INDEX, MINIMUM INDEX SALES

print("\n" + "="*50)
print("4) MAXIMUM, MINIMUM, MAXIMUM INDEX, MINIMUM INDEX SALES")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])

maximum = np.max(sales)
print("Maximum sales:", maximum)

minimum = np.min(sales)
print("Minimum sales:", minimum)

maximum_index = np.argmax(sales)
print("Index of maximum sales:", maximum_index)

minimum_index = np.argmin(sales)
print("Index of minimum sales:", minimum_index)


# 5) ACCESS ELEMENTS

print("\n" + "="*50)
print("5) ACCESS ELEMENTS")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])

print("First element:", sales[0])
print("Last element:", sales[-1])
print("Fifth element:", sales[4])
print("Elements from index 2 to 6:", sales[2:7])


# 6) REVERSE SALES ARRAY

print("\n" + "="*50)
print("6) REVERSE SALES ARRAY")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])
reverse = sales[::-1]

print("Reverse:", reverse)


# 7) SALES GREATER THAN 200

print("\n" + "="*50)
print("7) SALES GREATER THAN 200")
print("="*50)

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])
result = sales[sales > 200]

print("Sales greater than 200:", result)


# 8) AGE BETWEEN 25 AND 35

print("\n" + "="*50)
print("8) AGE BETWEEN 25 AND 35")
print("="*50)

ages = np.array([22, 35, 28, 41, 19, 32, 25, 45, 30, 27])
result = ages[(ages >= 25) & (ages <= 35)]

print("Ages between 25 and 35:", result)


# 9) STUDENTS MARKS

print("\n" + "="*50)
print("9) STUDENTS MARKS")
print("="*50)

marks = np.array([
    [85, 78, 92],
    [67, 75, 80],
    [90, 88, 95],
    [55, 60, 65],
    [72, 85, 78]
])

print("First student's marks:", marks[0])
print("Second student's marks:", marks[1])
print("First subject marks:", marks[:, 0])
print("Second subject marks:", marks[:, 1])


# 10) SUBJECT WISE AVERAGE

print("\n" + "="*50)
print("10) SUBJECT WISE AVERAGE")
print("="*50)

marks = np.array([
    [85, 78, 92],
    [67, 75, 80],
    [90, 88, 95],
    [55, 60, 65],
    [72, 85, 78]
])

average = np.mean(marks, axis=0)

print("Subject-wise Average:", average)


# 11) INCREASE PRICES BY 10%

print("\n" + "="*50)
print("11) INCREASE PRICES BY 10%")
print("="*50)

prices = np.array([100, 250, 150, 500, 350, 120, 450, 200])
new_prices = prices + (prices * 0.1)

print("Original Prices:", prices)
print("Prices after 10% increase:", new_prices)

print("\n" + "="*50)
print("ALL QUESTIONS COMPLETED")
print("="*50)