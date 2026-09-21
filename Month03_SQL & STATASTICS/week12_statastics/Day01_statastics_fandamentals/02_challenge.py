import numpy as np
import pandas as pd

sales = np.array([100, 150, 150, 200, 250, 1000])

df = pd.Series([100, 150, 150, 200, 250, 1000])

print(np.mean(sales))
print(np.median(sales))

print(df.mode())


