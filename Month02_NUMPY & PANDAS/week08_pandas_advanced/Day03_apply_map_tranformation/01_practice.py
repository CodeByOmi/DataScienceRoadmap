import pandas as pd 

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

#1 map()

df["Membership_Level"] = df["Membership"].map({
    "Basic": 1,
    "Premium": 2,
    "VIP": 3
})

df["Age_Double"] = df["Age"].map(lambda x: x * 2)

df["Age_5_years_later"] = df["Age"].map(lambda x: x + 5)

df["Height_m"] = df["Height_cm"].map(lambda x:x / 100)

#2 apply


df["Weight_group"] = df["Weight_kg"].apply(lambda x: "heavy" if x > 80 else "normal")

df["Age_type"] = df["Age"].apply(lambda x: "30+" if x >= 30 else "under 30")


#3 multiple candition

df["Membership_type"] = df["Membership"].map({
    "Basic" : "Low",
    "Premium" : "Medium", 
    "VIP" : "High"
    })

df["Training_group"] = df.apply(
    lambda row : "High-focus"
    if row["Weight_kg"] > 85 and row["Age"] > 25
    else "low-focus",
    axis=1
    )

print(df)


