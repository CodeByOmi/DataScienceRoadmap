import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "Product": [
        "Laptop","Phone","Tablet","Laptop","Phone",
        "Tablet","Laptop","Phone","Tablet","Laptop"
    ],

    "Sales": [
        800,500,300,900,600,
        350,750,550,400,1200
    ],

    "Quantity": [
        2,3,5,1,4,
        6,2,3,5,1
    ],

    "Profit": [
        150,80,40,200,100,
        70,140,90,50,300
    ]
})


# Task 1 — Basic EDA

print(df.shape)
print(df.info())
print(df.describe())




# Task 2 — Product Sales

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)




# Task 3 — Product Profit

product_profit = df.groupby("Product")["Profit"].sum()

print(product_profit)





# Task 4 — Product Quantity

product_quantity = df.groupby("Product")["Quantity"].sum()

print(product_quantity)




# Task 5 — Visualization

product_sales.plot(kind="bar")
plt.title("Sales by product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()




# Task 6 — Relationship

sns.scatterplot(data=df, x="Quantity", y="Sales")

plt.title("quantity vs sales")
plt.xlabel("quantity")
plt.ylabel("sales")
plt.show()

correlation = df["Quantity"].corr(df["Sales"])
print(correlation)



# Task 7 — Distribution

plt.hist(df["Sales"], bins=5)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()




# Task 8 — Outlier Check

sns.boxplot(y=df["Profit"])

plt.title("Profit Distribution")
plt.ylabel("Profit")

plt.show()




# Task 9 — Business Insights

# Insight 1 — Laptop dominates sales and profit

# Insight 2 — Tablet has the highest quantity but not the highest sales

# Insight 3 — Quantity isn't strongly driving sales here