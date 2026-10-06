import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Product": [
        "Laptop","Phone","Tablet","Laptop","Phone",
        "Tablet","Laptop","Phone","Tablet","Laptop",
        "Phone","Tablet"
    ],
    
    "Region": [
        "North","North","South","South","West",
        "West","East","East","North","South",
        "West","East"
    ],
    
    "Sales": [
        1200,500,300,900,600,
        350,1100,550,400,1300,
        450,320
    ],
    
    "Quantity": [
        1,3,5,1,4,
        6,2,3,5,1,
        4,6
    ],
    
    "Profit": [
        300,80,40,200,100,
        70,280,90,50,350,
        75,45
    ]
})



# Task 1 — Sales Distribution

sns.histplot(df["Sales"],kde=True)
plt.title("sales distribution")
plt.xlabel("Sales")
plt.ylabel("frequency")
plt.show()




# Task 2 — Product Analysis

print(df.groupby("Product")["Sales"].sum())
print(df.groupby("Product")["Profit"].sum())
print(df.groupby("Product")["Profit"].mean())




# Task 3 — Sales by Region + Product

region_product_sales = df.groupby(
    ["Region", "Product"]
)["Sales"].sum()

print(region_product_sales)




# Task 4 — Visualizations

product_sales = df.groupby("Product")["Sales"].sum()

plt.bar(product_sales.index, product_sales.values)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()


region_sales = df.groupby("Region")["Sales"].sum()

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


sns.scatterplot(
    data=df,
    x="Quantity",
    y="Sales"
)

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.show()




# Task 5 — Correlations

print(df["Sales"].corr(df["Quantity"]))
print(df["Sales"].corr(df["Profit"]))
print(df["Quantity"].corr(df["Profit"]))



# Task 6 — 3 Business Insights

# Insight 1 — Laptop performance

# Observation:
# Laptops generate ₹4,500 in sales and ₹1,130 in profit, much higher than phones and tablets.

# Possible explanation:
# Laptop transactions have much higher value per transaction.

# Business implication:
# The business should investigate whether maintaining strong laptop inventory could continue generating high-value sales.



# Insight 2 — South region
# Observation:
# South has the highest regional sales at ₹2,500.

# Possible explanation:
# The South region has particularly strong laptop sales, totaling ₹2,200.

# Business implication:
# The business could investigate what is different about the South region—customers, pricing, 
# demand, or product availability—and see whether the successful strategy can be replicated elsewhere


# Insight 3 — Quantity vs Sales

# Observation:
# Sales and Quantity have a very strong negative correlation of -0.9011.

# Possible explanation:
# Different products have very different prices. Tablets have higher quantities but lower-value transactions, while laptops have lower 
# quantities but much higher sales.

# Business implication:
# The company should not assume that increasing quantity automatically increases revenue. 
# Product mix and price per unit need to be investigated.