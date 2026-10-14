
# ============================================================
# WEEK 15 — EDA + DATA VISUALIZATION CHEAT SHEET
# ============================================================

# 1. DATA INSPECTION
df.head()                         # First 5 rows
df.shape                          # Rows and columns
df.info()                         # Column types and non-null counts
df.describe()                     # Summary statistics
df.isnull().sum()                 # Missing values
df.duplicated().sum()             # Duplicate rows

# 2. GROUPING AND COMPARISON
df.groupby("Product")["Sales"].sum()          # Total sales by product
df.groupby("Product")["Sales"].mean()         # Average sales
df.groupby("Region")[["Sales", "Profit"]].sum()  # Multiple metrics
df.groupby(["Region", "Product"])["Sales"].sum() # Multiple groups
df.groupby("Product").size()                  # Rows per product

# SORTING AND TOP PERFORMERS
df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
)                                  # Highest sales first

df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
).head(3)                          # Top 3 products

# 3. MATPLOTLIB — BASIC CHARTS
import matplotlib.pyplot as plt

plt.plot(monthly_sales)            # Trend over time
plt.bar(products, sales)           # Category comparison
plt.hist(df["Sales"], bins=10)     # Distribution
plt.scatter(df["Quantity"], df["Sales"])  # Relationship

plt.title("Chart Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. SEABORN — STATISTICAL VISUALIZATION
import seaborn as sns

sns.countplot(data=df, x="Product")  # Category counts
sns.boxplot(data=df, x="Product", y="Sales")  # Spread/outliers
sns.histplot(data=df, x="Sales", kde=True)    # Distribution
sns.scatterplot(
    data=df, x="Quantity", y="Sales", hue="Product"
)                                  # Relationship by group

sns.barplot(data=df, x="Product", y="Sales")  # Category comparison

# CORRELATION MATRIX
df.corr(numeric_only=True)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

# Correlation ranges from -1 to +1.
# Positive = variables tend to increase together.
# Negative = variables tend to move oppositely.
# Correlation DOES NOT prove causation.

# 5. SUBPLOTS AND VISUAL COMPARISON
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(sales)
axes[0].set_title("Sales")

axes[1].plot(profit)
axes[1].set_title("Profit")

plt.tight_layout()
plt.show()

# SEPARATE PLOTS BY CATEGORY
g = sns.FacetGrid(df, col="Product")
g.map_dataframe(sns.scatterplot, x="Quantity", y="Sales")
plt.show()

# PIVOT TABLE FOR COMPARISON
sales_table = df.pivot(
    index="Month", columns="Product", values="Sales"
)
print(sales_table)

# 6. DATES AND TIME TRENDS
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Monthly sales within each year
monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum()

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Year and Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Growth percentage
growth = (new_value - old_value) / old_value * 100

# 7. SEGMENTATION WITH pd.cut()
df["Segment"] = pd.cut(
    df["Sales"],
    bins=[0, 1000, 5000, float("inf")],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)

df.groupby("Segment", observed=True)["Sales"].sum()

# 8. LOSSES AND PROFIT MARGIN
losses = df[df["Profit"] < 0]      # Loss-making rows
len(losses)                        # Number of losses

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

profit_margin = total_profit / total_sales * 100
print(round(profit_margin, 2))

# 9. CORRELATION WITHIN EACH GROUP
print(df["Quantity"].corr(df["Sales"]))  # Overall correlation

for product in df["Product"].unique():
    product_data = df[df["Product"] == product]
    correlation = product_data["Quantity"].corr(
        product_data["Sales"]
    )
    print(product, correlation)

# Overall and within-group relationships can differ.
# Investigate product mix and other factors before concluding.

# 10. OUTLIER DETECTION USING IQR
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_bound) |
    (df["Sales"] > upper_bound)
]

# 11. BUSINESS INSIGHTS FRAMEWORK
# Observation -> What does the data show?
# Explanation -> What might explain the pattern?
# Impact      -> Why does it matter to the business?
# Next step   -> What should be investigated next?

# EDA WORKFLOW
# Inspect -> Clean -> Analyze -> Visualize
# -> Identify patterns -> Explain cautiously -> Next question

# IMPORTANT:
# Correlation != Causation
# High sales != High profit
# Outliers need investigation, not automatic deletion
# Use Year + Month when analyzing data across multiple years
