# Final Challenge — Predict monthly gym revenue 🏋️

# Scenario: A fitness chain wants to predict monthly revenue for its 
# gym branches based on membership and operating information.


import pandas as pd

gym = pd.DataFrame({
    "Members": [
        100, 120, 150, 180, 200,
        220, 250, 280, 300, 320,
        350, 380, 400, 420, 450,
        480, 500, 530, 550, 600
    ],
    "Trainers": [
        2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
        7, 7, 8, 8, 9, 9, 10, 10, 11, 12
    ],
    "Monthly_Fee": [
        1000, 1000, 1200, 1200, 1200,
        1300, 1300, 1400, 1400, 1400,
        1500, 1500, 1500, 1600, 1600,
        1600, 1700, 1700, 1800, 1800
    ],
    "Monthly_Revenue": [
        100000, 120000, 180000, 216000, 240000,
        286000, 325000, 392000, 420000, 448000,
        525000, 570000, 600000, 672000, 720000,
        768000, 850000, 901000, 990000, 1080000
    ]
})

print(gym)



x = gym[["Members","Trainers","Monthly_Fee"]]

y = gym["Monthly_Revenue"]

from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


models = {
    "Linear Regresion" : LinearRegression(),
    "Decision Tree" : DecisionTreeRegressor(max_depth=3),
    "Random Forest" : RandomForestRegressor(n_estimators=50, random_state=42)
    
}


from sklearn.model_selection import cross_val_score

results = []

for name, model in models.items():

    scores = cross_val_score(
        model,
        x,
        y,
        cv=kf,
        scoring="neg_mean_squared_error"
    )

    mse_scores = -scores

    results.append({
        "Model": name,
        "Mean_MSE": mse_scores.mean(),
        "Std_MSE": mse_scores.std()
    })

results_df = pd.DataFrame(results)

print(results_df)

results_df = results_df.sort_values(
    by="Mean_MSE"
)

print(results_df)

best_name = results_df.iloc[0]["Model"]

print("Selected model:", best_name)


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=42)

selected_model = LinearRegression()

selected_model.fit(x_train, y_train)

predictions = selected_model.predict(x_test)

test_mse = mean_squared_error(y_test, predictions)

print("Test MSE:", test_mse)