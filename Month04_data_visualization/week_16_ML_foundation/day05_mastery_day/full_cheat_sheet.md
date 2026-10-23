# WEEK 16 — MACHINE LEARNING CHEAT SHEET

# 1. FEATURES AND TARGET
X = df[["Feature1", "Feature2"]]  # Input features
y = df["Target"]                  # Target to predict

# 2. TRAIN-TEST SPLIT
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. MISSING VALUES AND DUPLICATES
df.isnull().sum()                 # Count missing values
df["Column"].fillna(df["Column"].median())  # Fill with median
df.duplicated().sum()             # Count duplicate rows
df.drop_duplicates()              # Remove verified duplicates

# 4. ENCODING AND SCALING
pd.get_dummies(df, columns=["Category"])  # Encode categories

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Fit preprocessing on training data only.

# 5. LINEAR REGRESSION — PREDICT NUMBERS
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Regression evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print(mean_absolute_error(y_test, predictions))  # MAE
print(mean_squared_error(y_test, predictions) ** 0.5)  # RMSE
print(r2_score(y_test, predictions))  # R²

# MAE: average absolute prediction error
# RMSE: penalizes large errors more strongly than MAE
# R²: comparison with a mean-based baseline; can be negative

# 6. LOGISTIC REGRESSION — CLASSIFICATION
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)  # Predicted classes
probabilities = model.predict_proba(X_test)[:, 1]  # Class 1 probability

# Convert probabilities to percentages
percentages = [round(p * 100, 2) for p in probabilities]

# 7. DECISION THRESHOLD
# Default binary classification threshold is typically 0.5.
# Probability >= threshold -> class 1
# Probability < threshold  -> class 0
# Higher threshold generally means fewer positive predictions.

# 8. CONFUSION MATRIX
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predictions))

# Binary matrix layout:
# [[TN, FP],
#  [FN, TP]]

# TP = Actual 1, predicted 1
# TN = Actual 0, predicted 0
# FP = Actual 0, predicted 1
# FN = Actual 1, predicted 0

# 9. PRECISION AND RECALL
from sklearn.metrics import precision_score, recall_score

print(precision_score(y_test, predictions))
print(recall_score(y_test, predictions))

# Precision = TP / (TP + FP)
# Recall    = TP / (TP + FN)

# 10. IMPORTANT ML RULES
# - Train on training data; evaluate on unseen test data.
# - Never fit preprocessing using test data.
# - Correlation does not automatically prove causation.
# - Accuracy can mislead when classes are imbalanced.
# - Choose metrics according to the cost of errors.
# - Do not automatically delete missing values or duplicates.