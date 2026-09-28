import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Product": ["Laptop","Phone","Tablet","Laptop","Phone",
                "Tablet","Laptop","Phone"],
    "Sales": [800,500,300,900,600,350,750,550],
    "Quantity": [2,3,5,1,4,6,2,3]
})


## product by sales

product_sales = df.groupby("Product")["Sales"].sum()

plt.bar(product_sales.index,product_sales.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()



## quantity vs sales

plt.scatter(df["Quantity"],df["Sales"])
plt.title("quantity vs sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()


## sales distribution 

plt.hist(df["Sales"], bins=3)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()


## insights 

##cInsight 1: Laptop generates the highest total sales (2450), so it contributes the most sales 
## revenue among the three products.

## Insight 2: Tablet has the lowest total sales (650) despite having some high quantities, 
## suggesting that its sales value per unit is relatively low.