

import pandas as pd

import pandas as pd

df = pd.DataFrame({
    "Region": ["North", "North", "South", "South", "West", "West"],
    "Sales":  [1000, 800, 1500, 500, 900, 700],
    "Profit": [200, -50, 300, 100, 150, -20]
})

print(df)



# Concept 1 — Compare groups using multiple metrics

result = df.groupby("Region")[["Sales", "Profit"]].sum()

print(result)





# Concept 2 — Find the best and worst performers

print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))




# Concept 3 — Analyze profit margins and loss-making transactions

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

margin = (total_profit / total_sales) * 100

print("Profit margin:", round(margin, 2), "%")


losses = df[df["Profit"] < 0]

print(losses)

print(len(losses))



# Concept 4 — Visualize findings and explain the business meaning

region_data = df.groupby("Region")[["Sales", "Profit"]].sum()

print(region_data)


import matplotlib.pyplot as plt

region_data.plot(kind="bar")

plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()