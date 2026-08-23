pd.read_csv()          → Load CSV

df.shape               → Rows & columns
df.columns             → Column names
df.info()              → Overall information
df.dtypes              → Data types

df.describe()          → Numerical statistics

df["col"].value_counts()
                       → Count categories

df.isna()              → Detect missing values
df.isna().sum()        → Missing count per column