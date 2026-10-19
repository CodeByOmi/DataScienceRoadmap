import pandas as pd 
import numpy as np


# Concept 1 — What is Machine Learning?

house_size = 1200

estimated_price = house_size * 3500

print("Estimated House price: ₹", estimated_price)



# Concept 2 — Traditional Programming vs Machine Learning

# Traditional programming: a rule written by us
sales = 12000

if sales >= 10000:
    print("High sales")
else:
    print("Regular sales")

#machince programmning

marks = 42

if marks >= 50:
    print("Pass")
else:
    print("Fail")




# Concept 3 — Features, labels and datasets

import pandas as pd

df = pd.DataFrame({
    "Advertising": [100, 200, 300, 400],
    "Visitors": [20, 35, 50, 65],
    "Sales": [500, 800, 1200, 1600]
})

X = df[["Advertising", "Visitors"]]
y = df["Sales"]

print("Features:")
print(X)

print("Target:")
print(y)




# Concept 5 — Training data vs testing data

from sklearn.model_selection import train_test_split

x = df[["Advertising", "Visitors"]]
y= df["Sales"]

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25, random_state=42)

print("Traing rows:", len(x_train))
print("Testing rows:", len(x_test))
print(x_train)
print(y_train)



# Concept 6 — Train a model and make predictions

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.DataFrame({
    "Advertising": [100, 150, 200, 250, 300, 350, 400, 450],
    "Visitors": [20, 25, 35, 40, 50, 55, 65, 70],
    "Sales": [500, 600, 800, 950, 1200, 1300, 1550, 1700]
})

x = df[["Advertising", "Visitors"]]
y = df["Sales"]


x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25, random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)

predictions = model.predict(x_test)

print("actual sales:")
print(y_test.tolist())

print("prdicted sales:")
print(predictions)