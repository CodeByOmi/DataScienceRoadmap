groupby()
→ split data into groups and perform calculations

df.groupby("Membership")["Weight_kg"].mean()

mean() → average
sum()  → total
count() → count non-null values
min() → minimum
max() → maximum

Multiple functions:
df.groupby("Membership")["Weight_kg"].agg(
    ["mean", "min", "max"]
)

Multiple columns:
df.groupby(
    ["Membership", "Gender"]
)["Weight_kg"].mean()

Multiple column aggregations:
df.groupby("Membership").agg({
    "Age": "mean",
    "Weight_kg": ["mean", "max"]
})

reset_index()
→ converts groupby index back into a column

sort_values(ascending=False)
→ highest to lowest