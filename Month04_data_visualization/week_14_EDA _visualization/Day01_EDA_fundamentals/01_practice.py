import pandas as pd


## Load and Inspect a Dataset

df = pd.read_csv("Month03_SQL & STATASTICS/week10_sql_intermediate/data/gym_members_clean.csv")

print(df.head(5))
print(df.shape)
print(df.columns)
print(df.info())


## missing values

df = pd.DataFrame({
    "Age": [20, 25, None, 30],
    "Salary": [25000, None, 40000, 50000]
})

print(df.isnull().sum())
print(df.isnull().any(axis=1))



## duplicate

df = pd.DataFrame({
    "Name": ["A", "B", "B", "C"],
    "Sales": [100, 200, 200, 300]
})

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df)



## descriptive stats

print(df.describe())

