import pandas as pd


df = pd.DataFrame({
    "Customers": [
        20, 30, 40, 50, 60, 70, 80, 90,
        100, 110, 120, 130, 140, 150, 160
    ],
    "Revenue": [
        4000, 5200, 6500, 8100, 9500,
        11200, 13000, 14500, 16000, 17800,
        19500, 21000, 22500, 23800, 25000
    ]
})

print(df)


X = df[["Customers"]]
y = df["Revenue"]

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

model_1 = LinearRegression()

model_2 = DecisionTreeRegressor(max_depth=1)

model_3 = DecisionTreeRegressor(max_depth=5)

model_4 = DecisionTreeRegressor(max_depth=10)


model_1.fit(X,y)
model_2.fit(X,y)
model_3.fit(X,y)
model_4.fit(X,y)



prediction_1 = model_1.predict(X)
prediction_2 = model_2.predict(X)
prediction_3 = model_3.predict(X)
prediction_4 = model_4.predict(X)


from sklearn.metrics import mean_squared_error


mse_1 = mean_squared_error(y,prediction_1)
mse_2 = mean_squared_error(y,prediction_2)
mse_3 = mean_squared_error(y,prediction_3)
mse_4 = mean_squared_error(y,prediction_4)


print(mse_1,mse_2,mse_3,mse_4)

print(prediction_1,prediction_2,prediction_3,prediction_4)
