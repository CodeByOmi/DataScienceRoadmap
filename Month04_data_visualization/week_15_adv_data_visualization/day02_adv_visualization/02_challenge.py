import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jan","Feb","Mar","Apr","May","Jun"
    ],

    "Product": [
        "Laptop","Laptop","Laptop","Laptop","Laptop","Laptop",
        "Phone","Phone","Phone","Phone","Phone","Phone"
    ],

    "Sales": [
        900,1000,1100,1200,1350,1500,
        500,550,600,650,700,750
    ],

    "Profit": [
        180,200,220,240,270,320,
        80,90,100,110,120,130
    ],

    "Quantity": [
        2,2,3,3,4,4,
        5,6,6,7,8,9
    ]
})


# Task 1 — Sales Trend

monthly_sales = (
    df.groupby(["Month", "Product"])["Sales"]
      .sum()
      .reset_index()
)

print(monthly_sales)

monthly_sales = df.pivot(
    index="Month",
    columns="Product",
    values="Sales"
)

print(monthly_sales)


monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()





# Task 2 — Product Comparison

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)

plt.bar(
    product_sales.index,
    product_sales.values
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()


# Task 3 — Product Sales Trend

monthly_sales = df.pivot(
    index="Month",
    columns="Product",
    values="Sales"
)

plt.plot(
    monthly_sales.index,
    monthly_sales["Laptop"],
    marker="o",
    label="Laptop"
)

plt.plot(
    monthly_sales.index,
    monthly_sales["Phone"],
    marker="o",
    label="Phone"
)

plt.title("Laptop vs Phone Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()


# Task 4 — Profit Distribution

sns.histplot(
    data=df,
    x="Profit",
    kde=True
)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.show()



# Task 5 — Sales vs Quantity

sns.scatterplot(
    data=df,
    x="Quantity",
    y="Sales",
    hue="Product"
)

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.show()

# Task 6 — FacetGrid

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