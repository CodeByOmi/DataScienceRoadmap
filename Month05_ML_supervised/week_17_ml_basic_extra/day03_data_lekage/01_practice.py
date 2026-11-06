import pandas as pd

df = pd.DataFrame({
    "Order_Value": [
        500, 1200, 800, 2000, 1500,
        700, 900, 2500, 1100, 1800,
        600, 2200, 1300, 400, 1700,
        1000, 3000, 750, 1600, 950
    ],

    "Delivery_Days": [
        2, 8, 3, 10, 7,
        2, 4, 12, 5, 9,
        3, 11, 6, 2, 8,
        4, 14, 3, 7, 5
    ],

    "Previous_Orders": [
        5, 1, 8, 2, 3,
        10, 4, 1, 6, 2,
        9, 1, 3, 12, 2,
        7, 1, 5, 3, 8
    ],

    "Refund_processed": [
        0, 1, 0, 1, 1,
        0, 0, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 1, 0, 1, 0
    ],

    "Cancelled": [
        0, 1, 0, 1, 1,
        0, 0, 1, 0, 1,
        0, 1, 1, 0, 1,
        0, 1, 0, 1, 0
    ]
})

print(df)



# Concept 1 — What is data leakage?

x = df[["Order_Value","Delivery_Days","Previous_Orders","Refund_processed"]]

y = df["Cancelled"]





# Concept 2 — Target leakage

x_correct = df.drop(columns=["Refund_processed","Cancelled"])
print(x_correct)





# Concept 3 — Train-test contamination

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x_correct, y , test_size=0.2 , random_state=42)

print(df.shape)
print(x_train.shape)
print(x_test.shape)




# Concept 4 — Data preprocessing leakage

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()

x_train_scaled = scalar.fit_transform(x_train)

x_test_scaled = scalar.transform(x_test)

print(x_train_scaled.shape)
print(x_test_scaled.shape)





# Concept 5 — Time leakage

sales = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5],
    "Today_Sales": [100, 120, 110, 140, 150],
    "Tomorrow_Sales": [120, 110, 140, 150, 160]
})



x = sales[["Today_Sales"]]

y = sales["Tomorrow_Sales"]


print(x,y)




# Concept 6 — How to prevent data leakage

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 

model = Pipeline([
    ("scaler",  StandardScaler()),
    ("classifier", LogisticRegression())
])

model.fit(x_train, y_train)

predictions = model.predict(x_test)

print(y_test)

print(predictions)