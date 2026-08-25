df.isna().sum() → missing values per column
df.isna().sum().sum() → total missing values

df.dropna() → remove rows with missing values
df.fillna(value) → fill missing values

mean() → average
median() → middle value
mode()[0] → most frequent value

df.duplicated().sum() → count duplicates
df.drop_duplicates() → remove duplicates