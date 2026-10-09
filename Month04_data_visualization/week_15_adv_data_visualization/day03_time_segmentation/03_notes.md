WEEK 15 DAY 3 — TIME + SEGMENTATION
====================================

DATES
-----
df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day


TIME ANALYSIS
-------------
df.groupby("Month")["Sales"].sum()


GROWTH
------
(New - Old) / Old × 100


SEGMENTATION
------------
pd.cut()

Example:
Low
Medium
High


SEGMENT COMPARISON
------------------
df.groupby("Segment")["Sales"].sum()


DEEPER EDA
----------
Overall pattern
      ↓
Split into groups
      ↓
Analyze each group
      ↓
Compare
      ↓
Find better explanation


KEY IDEA
--------
An overall pattern can hide
important group-level patterns.