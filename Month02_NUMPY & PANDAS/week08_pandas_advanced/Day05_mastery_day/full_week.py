import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")


#1 inspecting data

print(df.head(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())



#2 create messy data
messy = df.copy()

messy.loc[5, "Age"] = None
messy.loc[10, "Weight_kg"] = None
messy.loc[15, "Membership"] = None

messy.loc[0, "City"] = " pune "
messy.loc[1, "City"] = "MUMBAI "

messy = pd.concat(
    [messy, messy.iloc[[0, 1]]],
    ignore_index=True
)

print(messy.isna().sum().sum())
print(messy.duplicated().sum())

print(messy["City"].str.strip())