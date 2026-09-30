
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##1 seaborn

sales = [100, 150, 130, 200, 180]

sns.histplot(sales)

plt.show()

##2 count plot

products = ["Laptop", "Phone", "Laptop", "Tablet",
            "Phone", "Laptop", "Phone"]

sns.countplot(x=products)

plt.show()


products = ["A","B","A","C","B","A","C","B","A"]

sns.countplot(x=products)

plt.show()


##3 box plot


prices = [100,110,120,125,130,135,140,145,150,500]

sns.boxplot(x=prices)

plt.show()


##4 histogram + kde

data = np.random.normal(170, 8, 500)

sns.histplot(data, kde=True)

plt.show()

data = np.random.normal(500, 80, 1000)

sns.histplot(data, kde=True)

plt.show()


hours = [1,2,3,4,5,6]
marks = [40,45,55,60,70,80]

sns.scatterplot(x=hours, y=marks)

plt.show()


##5  Hue — Adding a Third Variable

df = pd.DataFrame({
    "Hours": [1,2,3,4,5,6],
    "Marks": [40,45,55,60,70,80],
    "Group": ["A","A","B","B","A","B"]
})

sns.scatterplot(
    data=df,
    x="Hours",
    y="Marks",
    hue="Group"
)

plt.show()



## Correlation Heatmap

df = pd.DataFrame({
    "Sales": [100,150,200,250,300],
    "Advertising": [10,20,30,40,50],
    "Customers": [20,30,40,50,60]
})


correlation = df.corr(numeric_only=True)

print(correlation)

sns.heatmap(correlation, annot=True)

plt.show()