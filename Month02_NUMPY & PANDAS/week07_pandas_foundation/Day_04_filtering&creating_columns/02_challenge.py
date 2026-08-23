import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

result = df[
    (df["Age"].between(20, 35)) &
    (df["Membership"].isin(["Premium", "VIP"])) &
    (df["Weight_kg"] > 70)
]

result = result.sort_values("Weight_kg", ascending=False)

result["Height_m"] = result["Height_cm"] / 100

result["BMI"] = result["Weight_kg"] / (result["Height_m"] ** 2)

result = result[["Name", "Age", "Weight_kg", "Membership", "BMI"]]

print(result)