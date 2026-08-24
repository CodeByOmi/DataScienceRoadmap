import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")


#1 filtering
print(df["Age"] > 30)


print(df[df["Age"] > 30])

print(df["Weight_kg"] <= 60)

print(df[df["Membership"] == "VIP"])



#2 multiple candition
print(df[(df["Age"] > 25) & (df["Weight_kg"] > 70)])

print(df[(df["Age"] < 20 ) | (df["Age"] > 35)])

print(df[~(df["Age"] > 30)])



#3 isin and between
print(df[df["Membership"].isin(["Premium","VIP"])])

print(df[df["Age"].between(20,25)])

print(df[df["Age"].between(20,30, inclusive="neither")])

print(df[df["Weight_kg"].between(60,80)])



#4 sorting
print(df.sort_values("Age"))

print(df.sort_values("Weight_kg", ascending=False))

print(df.sort_values(["Membership","Age"], ascending=[True,False]))



#5 creating and modify columns
df["Age_next_5_year"] = df["Age"] + 5


df["Weight_lbs"] = df["Weight_kg"] * 2.205


df["Height_m"] = df["Height_cm"] / 100


df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)
print(df)