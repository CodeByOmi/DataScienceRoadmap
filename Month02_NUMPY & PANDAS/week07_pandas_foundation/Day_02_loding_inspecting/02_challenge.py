import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")
print(df)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df["Membership"].value_counts(normalize=True)*100)
print(df.isna().sum())
print(df.isna().sum().sum())
