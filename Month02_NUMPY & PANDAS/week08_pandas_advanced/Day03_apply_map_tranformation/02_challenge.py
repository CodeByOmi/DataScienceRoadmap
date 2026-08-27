import pandas as pd
df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")


df["Membership_code"] = df["Membership"].map({
    "Basic" : 1,
    "Premium" : 2,
    "VIP" : 3
    })


df["Age_group"] = df["Age"].apply(
    lambda x: "above 30" if x >30 else "under 30"
    )


df["Weight_group"] = df["Weight_kg"].apply(
    lambda x: "Heavy" if x > 75 else "Normal"
)


df["Height_m"] = df["Height_cm"].map(lambda x: x / 100)



df["BMI"] = df["Weight_kg"] / (df["Height_m"]**2)


df["Priority"] = df.apply(
    lambda row: "High"
    if row["Membership"] == "VIP"
    and row["Weight_kg"] > 75
    else "Normal",
    axis=1)


print(df[["Name","Age","Age_group","Membership_code","Weight_group","Priority","BMI"]])



