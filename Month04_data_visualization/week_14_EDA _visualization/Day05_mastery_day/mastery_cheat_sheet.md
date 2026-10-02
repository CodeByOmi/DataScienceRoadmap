WEEK 14 — EDA + VISUALIZATION CHEAT SHEET
==========================================

EDA
---
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

GROUPBY
-------
df.groupby("Product")["Sales"].sum()
df.groupby("Product")["Sales"].mean()
df.groupby("Product")[["Sales","Profit"]].sum()

MATPLOTLIB
----------
plt.plot()       → Trend
plt.bar()        → Category comparison
plt.hist()       → Distribution
plt.scatter()    → Relationship

SEABORN
-------
sns.countplot()  → Category count
sns.boxplot()    → Spread + outliers
sns.histplot()   → Distribution
sns.scatterplot()→ Relationship
sns.heatmap()    → Correlation matrix

CORRELATION
-----------
df["Sales"].corr(df["Profit"])
df.corr(numeric_only=True)

+1 → Strong positive
 0 → No linear relationship
-1 → Strong negative

Correlation ≠ Causation

OUTLIERS
--------
IQR = Q3 - Q1

Lower = Q1 - 1.5 × IQR
Upper = Q3 + 1.5 × IQR

Below Lower OR Above Upper → Outlier

BUSINESS INSIGHT
----------------
Observation
→ Possible explanation
→ Business implication
→ Next question

EDA FLOW
--------
Inspect → Clean → Analyze → Visualize
→ Find patterns → Insights → Next question