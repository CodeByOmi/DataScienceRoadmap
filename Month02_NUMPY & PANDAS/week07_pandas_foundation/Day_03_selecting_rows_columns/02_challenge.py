import pandas as pd

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

print(df[["Name","Age","Membership"]])



print(df.loc[5,"Age"])
print(df.loc[0:2])




print(df.loc[0:2,["Name","Weight"]])
print(df.loc[0:5,["Name","Height","Age"]])



print(df.iloc[2])
print(df.iloc[2,1])
print(df.iloc[0:5,0:3])
print(df.iloc[5:10])
print(df.loc[0:10,["Age","Weight"]])
