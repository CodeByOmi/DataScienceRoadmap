import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Product": [
        "Laptop","Phone","Tablet","Laptop","Phone",
        "Tablet","Laptop","Phone","Tablet","Laptop",
        "Phone","Tablet"
    ],

    "Region": [
        "West","West","East","South","East",
        "West","North","South","East","North",
        "West","South"
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





# Mastery Task 1 — EDA Inspection

print(df.shape)
print(df.info())
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isna().sum())
print(df.duplicated().sum())






# Mastery Task 2 — Product Analysis

product_sales = df.groupby("Product")["Sales"].sum()
product_profit = df.groupby("Product")["Profit"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()

print(product_sales)
print(product_profit)
print(product_quantity)





# Mastery Task 3 — Region Analysis

regional_sales = df.groupby("Region")["Sales"].sum()
regional_avg_profit = df.groupby("Region")["Profit"].mean()

print(regional_sales)
print(regional_avg_profit)




# Mastery Task 4 — Visualization

product_sales.plot(kind="bar")
plt.title("salse by product")
plt.xlabel("product")
plt.ylabel("sales")
plt.show()



plt.hist(df["Sales"], bins=6)
plt.title("sales distribution")
plt.xlabel("sales")
plt.ylabel("frequency")
plt.show()



sns.scatterplot(data=df, x="Quantity", y="Sales")
plt.title("quantity vs sales")
plt.xlabel("quantity")
plt.ylabel("sales")
plt.show()






# Mastery Task 5 — Correlation

correlation = df.corr(numeric_only=True)

print(correlation)





# Mastery Task 6 — Heatmap

sns.heatmap(correlation,annot=True)
plt.title("correlation heatmap")
plt.show()




# Mastery Task 7 — Outlier Analysis

sns.boxplot(y=df["Profit"])
plt.title("profit outliers")
plt.show()


Q1 = df["Profit"].quantile(0.25)
Q3 = df["Profit"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(Q1,Q3,IQR,lower,upper)






# Mastery Task 8 Business Investigation


# Highest Sales

# Laptop → 4500

# Highest Profit

# Laptop → 1130

# Highest Quantity

# Tablet → 22



# pattern : Tablets are sold in the highest quantity, but laptops generate the highest sales and profit.



 

#Mastery Task 9  Final Mini EDA Report :


# Dataset
# Rows: 12
# Columns: 5
# Missing values: 0
# Duplicates: 0
# Products
# Highest Sales: Laptop — 4500
# Highest Profit: Laptop — 1130
# Highest Quantity: Tablet — 22
# Key relationships
# Sales ↔ Profit:   +0.992
# Sales ↔ Quantity: -0.901
# Quantity ↔ Profit: -0.858
# Outliers
# Profit outliers: None
# Main business finding
# Laptop → highest sales + highest profit
# Tablet → highest quantity
# North → highest average profit
