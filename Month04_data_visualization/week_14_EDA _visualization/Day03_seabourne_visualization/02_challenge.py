import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone",
                "Laptop","Tablet","Phone","Laptop","Phone"],
    "Sales": [800,500,800,300,600,900,350,550,750,450],
    "Quantity": [2,3,2,5,4,1,6,3,2,4],
    "Profit": [150,80,150,40,100,200,70,90,140,75]
})

## count plot

sns.countplot(data=df, x="Product")
plt.title("Number of Sales by Product")
plt.xlabel("Product")
plt.ylabel("Count")
plt.show()



## box plot

sns.boxplot(data=df, y="Product")
plt.title("Profit Distribution")
plt.ylabel("Profit")
plt.show()



## sales vs profit

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Product"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()


## Correlation Heatmap

correlation = df[["Sales", "Quantity", "Profit"]].corr()

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.show()


## business insights

# 1. Laptop and Phone have the highest number of observations, 
# with 4 each, while Tablet has 2.

# 2. Sales and Profit show a positive relationship in this dataset: 
# observations with higher sales generally tend to have higher profit.

# 3. The Profit box plot does not show an obvious extreme outlier, 
# so there isn't a clearly unusual profit value that needs immediate investigation.