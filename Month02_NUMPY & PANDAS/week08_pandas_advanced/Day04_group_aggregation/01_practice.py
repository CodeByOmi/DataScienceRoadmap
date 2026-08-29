import pandas as pd 

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")
#1 groupby

print(df.groupby("Membership")["Age"].min())

print(df.groupby("Membership")["Age"].max())

print(df.groupby("Membership")["Weight_kg"].max())


#2 multiple agg

print(df.groupby("Membership")["Age"].agg(["mean","max","min"]))

print(df.groupby("Membership").agg({
    "Age": "max",
    "Weight_kg": "mean",
    "Height_cm": ["min","max"]
}))

print(df.groupby(
    ["Membership", "Gender"]
)["Weight_kg"].mean())

result = df.groupby("Membership")["Weight_kg"].mean()
print(result)

result = result.reset_index()
# print(result)

result = df.groupby("City")["Weight_kg"].mean()

print(result.sort_values(ascending=False))
