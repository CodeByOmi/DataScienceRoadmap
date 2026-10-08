WEEK 15 DAY 2 — ADVANCED VISUALIZATION
======================================

SUBPLOTS
--------
fig, axes = plt.subplots(1, 2)

axes[0].plot(...)
axes[1].bar(...)


CHOOSE CHART BY QUESTION
------------------------
Line       → Time/trend
Bar        → Category comparison
Histogram  → Distribution
Box plot   → Spread + outliers
Scatter    → Relationship


HUE
---
Adds another categorical dimension.

sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    hue="Product"
)


FACETGRID
---------
Creates separate charts for categories.

g = sns.FacetGrid(df, col="Product")

g.map_dataframe(
    sns.scatterplot,
    x="Quantity",
    y="Sales"
)


TOP N
-----
df.groupby("Product")["Sales"] \
  .sum() \
  .sort_values(ascending=False) \
  .head(5)


DATA STORY
----------
Observation
→ Possible explanation
→ Business impact
→ Next question


KEY IDEA
--------
A chart is not the final answer.

Chart
→ Pattern
→ Explanation
→ Business implication
→ Investigation