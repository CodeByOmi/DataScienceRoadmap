import pandas as pd
import sqlite3

# Create database outside week10_sql_intermediate
conn = sqlite3.connect(
    "gym_database.db"
)

# CSV file paths
members = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/members.csv"
)

memberships = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/memberships.csv"
)

trainers = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/trainers.csv"
)

member_trainers = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/member_trainers.csv"
)

payments = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/payments.csv"
)

workouts = pd.read_csv(
    "Month03_SQL & STATASTICS/week10_sql_intermediate/Data/workouts.csv"
)

# Create tables
members.to_sql("members", conn, if_exists="replace", index=False)
memberships.to_sql("memberships", conn, if_exists="replace", index=False)
trainers.to_sql("trainers", conn, if_exists="replace", index=False)
member_trainers.to_sql("member_trainers", conn, if_exists="replace", index=False)
payments.to_sql("payments", conn, if_exists="replace", index=False)
workouts.to_sql("workouts", conn, if_exists="replace", index=False)

print("Database created successfully!")

# Close connection
conn.close()
