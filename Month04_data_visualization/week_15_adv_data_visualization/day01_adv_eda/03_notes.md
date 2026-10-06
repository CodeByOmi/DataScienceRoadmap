WEEK 15 DAY 1 — ADVANCED EDA
=============================

DISTRIBUTION
------------
Shows how values are spread.

Histogram → distribution
Mean + Median → numerical summary

Right skew → long tail toward large values
Left skew  → long tail toward small values


GROUPBY
-------
df.groupby("Region")["Sales"].sum()

df.groupby("Region")["Profit"].mean()

df.groupby(["Region","Product"])["Sales"].sum()


VISUAL GROUP COMPARISON
-----------------------
sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    hue="Product"
)


CORRELATION
-----------
df["Sales"].corr(df["Profit"])

+1 → strong positive
 0 → little/no linear relationship
-1 → strong negative

Correlation ≠ Causation


EDA INVESTIGATION
-----------------
Overall
  ↓
Groups
  ↓
Relationships
  ↓
Visualization
  ↓
Patterns
  ↓
Possible explanation
  ↓
Business implication
  ↓
Next question