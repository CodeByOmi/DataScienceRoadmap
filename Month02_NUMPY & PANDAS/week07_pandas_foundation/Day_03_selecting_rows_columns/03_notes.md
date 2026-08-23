df["Age"] → select one column
df[["Age","Weight"]] → select multiple columns

df.loc[row, "col"] → select by label
df.iloc[row, col] → select by position

loc[2:5] → 2 to 5 (5 included)
iloc[2:5] → 2 to 4 (5 excluded)