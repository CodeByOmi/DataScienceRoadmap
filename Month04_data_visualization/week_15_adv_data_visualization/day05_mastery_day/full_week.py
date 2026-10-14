import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Date": [
        "2025-01-05", "2025-01-12", "2025-01-20",
        "2025-02-04", "2025-02-11", "2025-02-22",
        "2025-03-03", "2025-03-15", "2025-03-25",
        "2025-04-05", "2025-04-14", "2025-04-23",
        "2025-05-02", "2025-05-13", "2025-05-25",
        "2025-06-04", "2025-06-16", "2025-06-27"
    ],
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet"
    ],
    "Region": [
        "North", "South", "West",
        "East", "North", "South",
        "West", "East", "North",
        "South", "West", "East",
        "North", "South", "West",
        "East", "North", "South"
    ],
    "Sales": [
        5000, 1800, 900,
        5500, 2000, 1000,
        6200, 2200, 1100,
        5800, 1900, 950,
        7000, 2500, 1300,
        7500, 2700, 1400
    ],
    "Quantity": [
        2, 6, 5,
        2, 7, 5,
        3, 7, 6,
        2, 6, 5,
        3, 8, 7,
        3, 8, 7
    ],
    "Profit": [
        800, 300, 100,
        900, 350, 120,
        1200, 400, -150,
        -500, 250, 100,
        1400, -200, 180,
        1600, 450, 200
    ]
})


# Task 1 — Data inspection and preparation

print(df.shape)

print(df.isna().sum())

print(df.duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

print(df)




# Task 2 — Product performance

total_sales_profit = df.groupby("Product")[["Sales","Profit"]].sum()
print(total_sales_profit)


avg_sales = df.groupby("Product")["Sales"].mean()
print(avg_sales)


rank_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(rank_products)


total_sales_profit.plot(kind="bar")
plt.title("revenue and profit chart")
plt.xlabel("products")
plt.ylabel("sales and profit")
plt.show()




# Task 3 — Regional performance

regional_data = df.groupby("Region")[["Sales","Profit"]].sum()
print(regional_data)

highest_region_profitable = df.groupby("Region")["Profit"].sum().sort_values(ascending=False).head(1)
print(highest_region_profitable)


regional_data.plot(kind="bar")
plt.show()





# Task 4 — Losses and profit margins

losses = df[df["Profit"] <0]
print(losses)
print(len(losses))

total_sales = df.groupby("Product")["Sales"].sum()

total_profit =df.groupby("Product")["Profit"].sum()

margin = (total_profit / total_sales) * 100

print("margin:" , round(margin,2), "%")





# Task 5 — Monthly trends and correlation

monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)


monthly_sales.plot(kind="line",marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()



correlation = df["Quantity"].corr(df["Sales"])
print(correlation)



# Task 6 — Business insights

# insight 1 : Task 6 — Business insights

# Insight 2: Sales generally increase over time

# Insight 3: Some transactions generate losses