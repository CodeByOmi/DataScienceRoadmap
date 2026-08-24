import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")


#1 initial inception 
print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.describe())


#2 membership analysis

print(df["Membership"].value_counts())

print((df["City"] == "Pune").sum())

print((df["Membership"] == "VIP").mean() *100) #not correct



#3 member filtering
result = df[
            (df["Age"].between(20,30)) &
            (df["Membership"].isin(["Premium","VIP"])) &
            (df["Weight_kg"] > 70)
            ]

print(result.sort_values("Weight_kg" , ascending=False))

result = result[["Name","Age","Weight_kg","Membership","City"]]



#4 create useful columns
df["Weight_lbs"] = df["Weight_kg"] * 2.205

df["Height_m"] = df["Height_cm"] / 100

df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

print(df)
#5 advanced filtering

new = df[
        (df["BMI"] > 25) &
        (df["Age"].between(20,35)) &
        (df["Membership"].isin(["Basic","VIP"]))
        ]

new = new[["Name","Age","Weight_kg","Membership","BMI"]]

print(new)

vip_city = df[df["Membership"] == "VIP"]["City"].value_counts()

print(vip_city)
