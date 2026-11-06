import pandas as pd

hospital = pd.DataFrame({
    "Patient_Age": [25, 60, 45, 70, 35, 55, 80, 40, 65, 30],
    "Previous_Admissions": [0, 3, 1, 4, 0, 2, 5, 1, 3, 0],
    "Hospital_Stay_Days": [2, 8, 4, 10, 3, 6, 12, 5, 9, 2],
    "Followup_Visits": [2, 0, 1, 0, 3, 1, 0, 2, 0, 3],
    "Readmitted": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    "Readmission_Treatment": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
})

print(hospital)


x = hospital[["Patient_Age","Previous_Admissions","Hospital_Stay_Days","Followup_Visits"]]

y = hospital["Readmitted"]


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.25, random_state=42)

from sklearn.pipeline import Pipeline 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


model = Pipeline([
    ("Scaler", StandardScaler()),
    ("Classifier", LogisticRegression())
])

model.fit(x_train,y_train)

predictions = model.predict(x_test)

accuracy = accuracy_score(y_test, predictions)

print("Actual:", y_test.values)
print("Predicted:", predictions)

print(predictions)
print(accuracy)