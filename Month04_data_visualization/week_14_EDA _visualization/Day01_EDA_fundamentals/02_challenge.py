import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone",
                "Laptop","Tablet","Phone","Laptop","Phone"],
    "Sales": [800,500,800,300,450,900,350,500,750,450],
    "Quantity": [2,3,2,5,4,1,6,3,2,4]
})

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())

print(df.describe())

print(df["Product"].value_counts())

