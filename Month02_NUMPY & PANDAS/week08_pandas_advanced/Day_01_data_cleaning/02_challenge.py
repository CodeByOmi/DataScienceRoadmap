import pandas as pd
df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")
messy_df = df.copy()

messy_df.loc[5, "Age"] = None
messy_df.loc[10, "Weight_kg"] = None
messy_df.loc[15, "Membership"] = None

messy_df = pd.concat(
    [messy_df, messy_df.iloc[[0, 1]]],
    ignore_index=True
)

print(messy_df.isna().sum().sum())

print(messy_df.duplicated().sum())

messy_df["Age"] = messy_df["Age"].fillna(messy_df["Age"].median())

messy_df["Weight_kg"] = messy_df["Weight_kg"].fillna(messy_df["Weight_kg"].mean())

messy_df["Membership"] = messy_df["Membership"].fillna(messy_df["Membership"].mode()[0])

print(messy_df)

messy_df = messy_df.drop_duplicates()

print("Missing:", messy_df.isna().sum().sum())
print("Duplicates:", messy_df.duplicated().sum())