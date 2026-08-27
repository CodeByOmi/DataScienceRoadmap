import pandas as pd 

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

#1 astpye

test_df = df.copy()

print(test_df["Age"].dtypes)

print(test_df.dtypes)

test_df["Age"] = test_df["Age"].astype(float)

print(test_df["Age"].dtype)

print(test_df["Age"])

test_df["Months_Member"] = test_df["Months_Member"].astype(str)

print(test_df["Months_Member"])

print(test_df["Weight_kg"].dtype)





#2 pd.to_numeric()

test = pd.Series(["10", "20", "abc", "30", "unknown"])
print(test)
test = pd.to_numeric(test, errors="coerce")

print(test.isna().sum())

test= test.fillna(test.median())

print(test)


#3 .str methods

test_df["Name"] = test_df["Name"].str.upper()

test_df["City"] = test_df["City"].str.lower()

test_df["Membership"] = test_df["Membership"].str.strip()

print(test_df)



#4 str.contains

print(test_df[test_df["City"].str.contains("Pune", case=False, na=False)])

print(test_df[test_df["Name"].str.contains("a", case=False, na=False)])

print(test_df[test_df["Membership"].str.contains("Premium", case=False, na=False)])