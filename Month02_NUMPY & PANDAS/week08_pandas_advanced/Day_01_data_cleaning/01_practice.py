import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

#1 detecting missing values

clean_df = df.copy()

clean_df.loc[5, "Age"] = None
clean_df.loc[10, "Weight_kg"] = None
clean_df.loc[15, "Membership"] = None

# print(clean_df.isna().sum())

# print(clean_df.isna().sum().sum())

# print(clean_df.columns[clean_df.isna().any()])



# remove missing values
# print(clean_df.dropna())

# print(clean_df.dropna(subset=["Membership"]))

# print(clean_df.dropna(subset=["Age","Weight_kg"]))




#3 replacing missing vLUES

# clean_df["Age"] = clean_df["Age"].fillna(clean_df["Age"].median())

# clean_df["Weight_kg"] = clean_df["Weight_kg"].fillna((clean_df["Weight_kg"].mean()))

# clean_df["Membership"] = clean_df["Membership"].fillna(clean_df["Membership"].mode()[0])
# print(clean_df)



#4 
duplicate_df = df.copy()

duplicate_df = pd.concat(
    [duplicate_df, duplicate_df.iloc[[0, 1]]],
    ignore_index=True
)

print(duplicate_df.duplicated().sum())

print(duplicate_df[duplicate_df.duplicated()])

print(
duplicate_df.duplicated(subset=["Member_ID"]).sum())

