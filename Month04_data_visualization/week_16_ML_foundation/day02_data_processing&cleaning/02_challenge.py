import pandas as pd

df = pd.DataFrame({
    "Age": [22, 35, None, 28, 35, 40],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune"],
    "Salary": [25000, 40000, 30000, None, 40000, 50000],
    "Purchased": [0, 1, 0, 1, 1, 1]
})

print(df)



# Task 1 — Inspect: Print the missing-value counts and duplicate count.

print("missing values:", df.isna().sum().sum())
print("duplicated rows:", df.duplicated().sum())



# Task 2 — Clean: Fill missing Age and Salary using their respective medians. Remove genuine duplicate rows, if any.

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)


df = df.drop_duplicates()

print(df)




# Task 3 — Encode: One-hot encode the City column and display the result.

encoded = pd.get_dummies(df , columns=["City"], dtype=int)

print(encoded)






# Task 4 — Scale: Apply StandardScaler to Age and Salary.
# For this small exercise, practice the transformation on the cleaned data; in a real ML workflow, fit it on the training subset only.


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df["age_scaled"] = scaler.fit_transform(df[["Age"]])

df["Salary_scaled"] = scaler.fit_transform(df[["Salary"]])

print(df)