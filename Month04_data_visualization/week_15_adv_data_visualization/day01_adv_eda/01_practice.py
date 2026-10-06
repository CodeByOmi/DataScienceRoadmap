# CONCEPT 1 — Understanding Distributions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = [100,110,120,125,130,135,140,150,800]

print("Mean:", sum(sales) / len(sales))
print("Median:", pd.Series(sales).median())

sns.histplot(sales, kde=True)
plt.show()




# CONCEPT 2 — Grouped EDA

df = pd.DataFrame({
    "Region": ["North","North","South","South","West","West"],
    "Sales": [1000,1200,800,900,500,700],
    "Profit": [200,250,150,180,80,100]
})

regional_analysis = df.groupby("Region")[["Sales","Profit"]].sum()

print(regional_analysis)


print(df.groupby("Region")["Profit"].mean())

print(df.groupby("Region").size())




# CONCEPT 3 — Multi-Level Grouping

df = pd.DataFrame({
    "Region": ["North","North","North","South","South","South"],
    "Product": ["Laptop","Phone","Laptop","Laptop","Phone","Phone"],
    "Sales": [1000,500,1200,800,700,900]
})

result = df.groupby(["Region", "Product"])["Sales"].sum()

print(result)


print(df.groupby(["Region","Product"])["Sales"].max())





# CONCEPT 4 — Comparing Groups Visually

region_sales = df.groupby("Region")["Sales"].sum()

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    hue="Product"
)

plt.show()




# CONCEPT 5 — Finding Relationships Between Variables

df = pd.DataFrame({
    "Ad_Spend": [10,20,30,40,50,60],
    "Sales": [100,150,210,280,350,430]
})

correlation = df["Ad_Spend"].corr(df["Sales"])

print(correlation)

sns.scatterplot(data=df,x="Ad_Spend",y="Sales")
plt.show()


