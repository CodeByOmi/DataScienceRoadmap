import pandas as pd
df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

messy = df.copy()

messy.loc[0, "City"] = " pune "
messy.loc[1, "City"] = "MUMBAI "
messy.loc[2, "Membership"] = " premium"
messy.loc[3, "Membership"] = "VIP "


messy["City"] = messy["City"].str.strip()
messy["Membership"] = messy["Membership"].str.strip()

messy["City"] = messy["City"].str.lower()

messy[messy["City"].str.contains("pune", na=False)]

messy["Name_Clean"] = messy["Name"].str.upper()

print(messy)

test = pd.Series(["100", "200", "abc", "300"])

test = pd.to_numeric(test, errors="coerce")

print(test)
print(test.isna().sum())