import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": [
        "2025-01-05","2025-01-15","2025-02-10",
        "2025-02-20","2025-03-05","2025-03-15",
        "2025-04-10","2025-04-20","2025-04-05",
        "2025-05-15","2025-06-10","2025-06-20"
    ],

    "Product": [
        "Laptop","Phone","Laptop","Phone",
        "Laptop","Phone","Laptop","Phone",
        "Laptop","Phone","Laptop","Phone"
    ],

    "Sales": [
        1000,500,1100,550,
        1200,600,1300,650,
        1400,700,1500,750
    ],

    "Quantity": [
        2,5,2,6,
        3,6,3,7,
        4,8,4,9
    ]
})

# Task 1 — Date Preparation

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

print(df)




# Task 2 — Monthly Sales

monthly_sale = df.groupby("Month")["Sales"].sum()

print(monthly_sale)


plt.plot(monthly_sale.index, monthly_sale.values, marker="o")

plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()




# Task 3 — Product Comparison

print(df.groupby("Product")["Sales"].sum())
print(df.groupby("Product")["Sales"].mean())




# Task 4 — Product segmentation


df["Segment"] = df["Product"].map({
    "Laptop": "Premium",
    "Phone": "Standard"
})

print(df.groupby("Segment")["Sales"].sum())




# Task 5 — Correlation

print(df["Quantity"].corr(df["Sales"]))

for product in df["Product"].unique():
    product_data = df[df["Product"] == product]

    correlation = product_data["Quantity"].corr(
        product_data["Sales"]
    )

    print(product, correlation)