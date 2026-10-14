import pandas as pd

df = pd.DataFrame({
    "Product": [
        "Laptop", "Phone", "Tablet", "Laptop",
        "Phone", "Tablet", "Laptop", "Phone",
        "Tablet", "Laptop", "Phone", "Tablet"
    ],
    "Region": [
        "North", "North", "South", "South",
        "West", "West", "East", "East",
        "North", "South", "West", "East"
    ],
    "Sales": [
        5000, 2000, 800, 4000, 2500, 1000,
        6000, 1800, 1200, 3000, 2200, 900
    ],
    "Profit": [
        800, 300, 100, 700, -200, 150,
        1200, 250, -100, -500, 350, 120
    ]
})



# 1 product performance

total_sales = df.groupby("Product")["Sales"].sum()

total_profit = df.groupby("Product")["Profit"].sum()

print("total_sales :",total_sales)
print("total_profit :",total_profit)



# 2 regional performance

regional_performance = df.groupby("Region")[["Sales","Profit"]].sum()

print("regional_performance :",regional_performance)




# 3 loss investigation

losses = df[ df["Profit"] <0 ]

print(losses)
print(len(losses))




#4 profit margin

profit_margin = (total_profit / total_sales) * 100

print("profit margin:", round(profit_margin,2), "%")




#5 visualization
import matplotlib.pyplot as plt

total_sales = df.groupby("Product")["Sales"].sum()

total_sales.plot(kind="bar")

plt.title("sales by product")
plt.xlabel("product")
plt.ylabel("slaes")
plt.show()