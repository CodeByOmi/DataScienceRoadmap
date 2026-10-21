import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Missing values
df.isnull().sum()
df["Age"] = df["Age"].fillna(df["Age"].median())

# Duplicate rows
df.duplicated().sum()
df = df.drop_duplicates()

# Encode categories
df["City"] = df["City"].map({"Pune": 0, "Mumbai": 1})

# Standardization
scaler = StandardScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])

# Normalization: scale values to 0–1
scaler = MinMaxScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])