# Scenario: Predict sales for a small shop

import pandas as pd

df = pd.DataFrame({
    "Advertising": [100, 120, 150, 180, 200, 220,
                    250, 280, 300, 320, 350, 400],
    "Visitors": [20, 22, 25, 30, 35, 38,
                 42, 48, 50, 55, 60, 68],
    "Sales": [450, 500, 600, 680, 750, 820,
              900, 1050, 1100, 1200, 1350, 1500]
})



# Task 1 — Understand the data

print(df.shape)
print(df.info())

x = df[["Advertising","Visitors"]]
y = df["Sales"]



# Task 2 — Prepare the data

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25, random_state=42)

print("Training rows:", len(x_train))
print("Testing rows:", len(x_test))



# Task 3 — Train the model

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train,y_train)



# Task 4 — Make predictions

predictions = model.predict(x_test)

print("actual sales")
print(y_test.tolist())

print("predicted sales")
print(predictions)


