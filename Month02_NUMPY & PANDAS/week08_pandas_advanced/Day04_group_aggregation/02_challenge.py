import pandas as pd 

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

result = df.groupby("Membership")["Name"].count()

print(result.sort_values(ascending=False))

result = df.groupby("City").agg({
    "Name": "count",
    "Age": "mean",
    "Weight_kg": "mean"
})

print(result)

result = df.groupby("Membership")["Weight_kg"].mean()

print(result.sort_values(ascending=False))

result = df.groupby(
    ["Membership", "Gender"]
)["Weight_kg"].mean()

print(result)

result = df.groupby("City").agg(
    Member_Count=("Name", "count"),
    Average_Weight=("Weight_kg", "mean")
)

result = result.reset_index()

result = result.sort_values(
    "Member_Count",
    ascending=False
)

print(result)

df.groupby("City").agg(
    Member_Count=("Name", "count"),
    Average_Weight=("Weight_kg", "mean")
)