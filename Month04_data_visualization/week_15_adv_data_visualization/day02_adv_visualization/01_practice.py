# CONCEPT 1 — Subplots: Multiple Charts in One Figure
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = [100,200,300,400,500]
profit = [20,50,70,100,120]

fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(sales)
axes[0].set_title("Sales")

axes[1].plot(profit)
axes[1].set_title("Profit")

plt.tight_layout()
plt.show()




# CONCEPT 2 — hue: Adding Another Dimension

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


sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    hue="Product"
)

plt.title("Sales by Region and Product")
plt.show()





# CONCEPT 3 — Small Multiples with FacetGrid

g = sns.FacetGrid(
    df,
    col="Product"
)

g.map_dataframe(
    sns.scatterplot,
    x="Quantity",
    y="Sales"
)

plt.show()




# CONCEPT 6 — Highlighting What Matters\

products = {
    "Laptop": 5000,
    "Phone": 4200,
    "Tablet": 3000,
    "Monitor": 2500,
    "Keyboard": 1800,
    "Mouse": 1200,
    "Printer": 900
}

sales = pd.Series(products)

top3 = sales.sort_values(ascending=False).head(3)

print(top3)

plt.bar(top3.index, top3.values)

plt.title("Top 3 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()




