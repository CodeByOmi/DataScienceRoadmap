import pandas as pd
import sqlite3

df = pd.read_csv("Month02_NUMPY & PANDAS/week07_pandas_foundation/data/gym_members.csv")

conn = sqlite3.connect("gym.db")

df.to_sql("gym_members", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")