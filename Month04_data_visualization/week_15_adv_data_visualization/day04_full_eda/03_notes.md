# Rank high to low
series.sort_values(ascending=False)

# Find lowest value
series.sort_values().head(1)

# Select top 2
series.sort_values(ascending=False).head(2)

# Group by product
df.groupby("Product")["Sales"].sum()

# Group by two columns
df.groupby(["Product", "Region"])["Sales"].sum()

# Calculate profit margin
summary = df.groupby("Product")[["Sales", "Profit"]].sum()
summary["Profit_Margin"] = summary["Profit"] / summary["Sales"] * 100