
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


##1 insights
df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Sales": [800, 500, 300, 900, 600, 350]
})

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)
print(product_sales.idxmin())



##2 Univariate Patterns

import matplotlib.pyplot as plt

sales = [100, 120, 150, 200, 220, 250, 300, 500, 800, 1200]

plt.hist(sales, bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

 
##3 bivarient patterns

df = pd.DataFrame({
    "Quantity": [1,2,3,4,5,6,7,8],
    "Sales": [100,180,250,330,420,500,620,700]
})

sns.scatterplot(data=df, x="Quantity", y="Sales")

plt.title("Quantity vs Sales")
plt.show()

correlation = df["Sales"].corr(df["Quantity"])

print(correlation)



##4 group camparisons


import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop","Phone","Tablet","Laptop","Phone","Tablet"],
    "Sales": [800,500,300,900,600,350],
    "Profit": [150,80,40,200,100,70]
})

result = df.groupby("Product")[["Sales","Profit"]].sum()

print(result)


result["Sales"].plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()


result["Profit"].plot(kind="bar")
plt.title("profit by product")
plt.xlabel("product")
plt.ylabel("profit")
plt.show()



## 5 Outliers & Anomalies

import pandas as pd

df = pd.DataFrame({
    "Sales": [100,120,130,140,150,1450]
})

print(df.describe())

sns.boxplot(y=df["Sales"])

plt.title("Sales Outliers")
plt.show()



profit = [50,60,55,70,65,500,-200]

sns.boxplot(y=profit)
plt.title("profit ouliers")
plt.show()




## 6 Segment Analysis

import pandas as pd

df = pd.DataFrame({
    "Customer": ["A","B","C","D","E","F"],
    "Type": ["New","Returning","New","Returning","New","Returning"],
    "Sales": [100,300,150,500,120,450]
})

result = df.groupby("Type")["Sales"].agg(["sum","mean","count"])

print(result)


## 7 Turning a Chart Into a Business Insight

#OBSERVATION
    #  ↓
#POSSIBLE EXPLANATION
    #  ↓
# BUSINESS IMPLICATION
    #  ↓
# NEXT QUESTION