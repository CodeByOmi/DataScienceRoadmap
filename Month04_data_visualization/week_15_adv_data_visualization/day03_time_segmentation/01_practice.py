import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CONCEPT 1 — Time-Based EDA

df = pd.DataFrame({
    "Date": [
        "2025-01-05",
        "2025-02-10",
        "2025-02-20",
        "2026-01-15"
    ],
    "Sales": [100,150,200,300]
})


df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month

df["Day"] = df["Date"].dt.day


print(df)




# CONCEPT 2 — Sales Trends Over Time

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()





# CONCEPT 3 — Year-over-Year Comparison

yearly_sales = pd.Series({
    2024: 100000,
    2025: 125000
})

yearly_sales = df.groupby("Year")["Sales"].sum()
print(yearly_sales)





# CONCEPT 4 — Segmentation

df = pd.DataFrame({
    "Customer": ["A","B","C","D"],
    "Sales": [200,5000,800,12000],
    
})

df["Segment"] = pd.cut(
    df["Sales"],
    bins=[0,1000,5000,20000],
    labels=["Low","Medium","High"]
)

print(df)





# CONCEPT 5 — Comparing Segments

segment_sales = df.groupby("Segment",observed=True)["Sales"].sum()

print(segment_sales)

plt.bar(
    segment_sales.index,
    segment_sales.values
)

plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")

plt.show()




# CONCEPT 6 — Overall Pattern vs Group Pattern


# print(df["Customer"].corr(df["Sales"]))


# for product in df["Product"].unique():

#     product_data = df[df["Product"] == product]

#     correlation = product_data["Quantity"].corr(
#         product_data["Sales"]
#     )

#     print(product, correlation)