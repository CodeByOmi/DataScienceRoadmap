EDA = Exploratory Data Analysis

df.head()       → first rows
df.tail()       → last rows
df.shape        → rows, columns
df.columns      → column names
df.info()       → data types + missing info
df.describe()   → statistics

df.isnull().sum()       → missing values
df.duplicated().sum()   → duplicates
df.drop_duplicates()    → remove duplicates

df["col"].mean()
df["col"].median()
df["col"].min()
df["col"].max()
df["col"].std()

df["col"].value_counts() → category frequency