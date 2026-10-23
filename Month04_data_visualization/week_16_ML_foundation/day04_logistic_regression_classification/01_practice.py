# Concept 1 — Probability and predict_proba()

import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1]
})

x = df[["Hours"]]
y = df["Passed"]

model = LogisticRegression()
model.fit(x, y)

new_students = pd.DataFrame({
    "Hours": [3, 5, 7]
})

predictions = model.predict(new_students)
print(predictions)


probabilities = model.predict_proba(new_students)
print((probabilities*100).round(2))

pass_probabilities = probabilities[:, 1]
print(pass_probabilities)

for probability in pass_probabilities:
    percentage = round(probability * 100, 2)
    print(percentage, "%")





# Concept 2 — Decision thresholds

probability = 0.72
threshold = 0.5

if probability >= threshold:
    prediction = 1
else:
    prediction = 0

print(prediction)


probability = 0.72
threshold = 0.80

if probability >= threshold:
    prediction = 1
else:
    prediction = 0

print(prediction)





# Concept 3 — Decision boundaries

test_students = pd.DataFrame({
    "Hours": [2, 4, 5, 7]
})

predictions = model.predict(test_students)

print(predictions)






# Concept 4 — Interpret predictions and probabilities together

probabilities = model.predict_proba(new_students)
pass_probabilities = probabilities[:, 1]

for probability in pass_probabilities:
    if probability >= 0.5:
        print("Predicted Pass")
    else:
        print("Predicted Fail")





# Concept 5 — Confusion matrix: TP, FP, TN, FN


from sklearn.metrics import confusion_matrix

actual = [0, 0, 0, 1, 1, 1]
predicted = [0, 0, 1, 1, 0, 1]

matrix = confusion_matrix(actual, predicted)
print(matrix)




# Concept 6 — Class imbalance, precision, and recall

from sklearn.metrics import precision_score, recall_score

actual = [0, 0, 0, 1, 1, 1]
predicted = [0, 0, 1, 1, 0, 1]

print("Precision:", precision_score(actual, predicted))
print("Recall:", recall_score(actual, predicted))