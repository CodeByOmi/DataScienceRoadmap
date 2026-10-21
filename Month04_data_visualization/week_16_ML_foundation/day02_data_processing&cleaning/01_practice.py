import pandas as pd

df = pd.DataFrame({
    "Customer": ["A", "B", "C", "C"],
    "Age": [22, None, 35, 35],
    "City": ["Pune", "Mumbai", "Pune", "Pune"],
    "Spending": [500, 800, 650, 650]
})

print(df)



# Concept 1 — Why data preprocessing matters

print(df.isna().sum())
print(df.duplicated())



# Concept 2 — Handling missing values

import pandas as pd

df = pd.DataFrame({
    "Marks": [40, 60, None, 80, 100]
})


print(df.isna().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)
print(df.isna().sum())




# Concept 3 — Detecting and removing duplicates

import pandas as pd

df = pd.DataFrame({
    "Product": ["Pen", "Book", "Pen"],
    "Price": [10, 50, 10]
})

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df)

print(df.duplicated().sum())




# Concept 4 — Encoding categorical data

import pandas as pd

df = pd.DataFrame({
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"]
})

df["city_code"] = df["City"].map({
    "Pune": 0,
    "Mumbai":1
})

print(df)



df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green"]
})

encoded = pd.get_dummies(df, columns=["Color"], dtype=int)

print(encoded)




# Concept 5 — Feature scaling: standardization and normalization

from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 30, 40]
})

scaler = StandardScaler()
df["Age_Scaled"] = scaler.fit_transform(df[["Age"]])

print(df)


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df["Age_Normalized"] = scaler.fit_transform(df[["Age"]])

print(df)