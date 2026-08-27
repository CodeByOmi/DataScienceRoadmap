map() → transform values in a Series

df["x"].map({"Basic": 1, "VIP": 3})

lambda x: x * 2
→ small anonymous function

df["x"].apply(lambda x: x * 2)
→ apply function to each value

lambda x: "A" if x > 50 else "B"
→ conditional transformation

df.apply(function, axis=1)
→ apply row by row

axis=0 → column-wise
axis=1 → row-wise

Prefer vectorized operations when possible:
df["Age"] + 5
better than
df["Age"].apply(lambda x: x + 5)