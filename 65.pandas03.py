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


# Total Price
df["total_price"] = df["price"] * df["quantity"]


# 10% Discount if total_price >= 5000
df["discount"] = np.where(
    df["total_price"] >= 5000,
    df["total_price"] * 0.10,
    0
)


# Delivery (2000 or above = Free)
df["delivery"] = np.where(
    df["total_price"] >= 2000,
    0,
    100
)


# GST 8%
df["gst"] = (df["total_price"] - df["discount"]) * 0.08


# Final Total Price
df["final_total_price"] = (
    df["total_price"]
    - df["discount"]
    + df["gst"]
    + df["delivery"]
)


print(df)