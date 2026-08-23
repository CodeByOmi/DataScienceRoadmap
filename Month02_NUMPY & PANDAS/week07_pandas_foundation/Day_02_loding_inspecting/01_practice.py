import pandas as pd

# csv

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")
print(df)

preview = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv", nrows=4)
print(preview)

demo = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv" ,nrows=5)
print(demo)


#structure
print(df.info())
print(df.dtypes)
print(df["Age"].dtypes)
print(df["Membership"].dtypes)

# #describe

print(df.describe())
print(df["Age"].describe())
print(df["Weight"].mean())



# #catogarical data
print(df.describe(include="all"))

print(df["Membership"].value_counts(normalize=True)*100)
print(df["Gender"].value_counts())

# #mising values
print(df["Height"].isna().sum().sum())
print(df.notna())
