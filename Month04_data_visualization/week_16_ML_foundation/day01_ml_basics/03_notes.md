
# WEEK 16 — DAY 1: MACHINE LEARNING FUNDAMENTALS

# 1. FEATURES AND TARGET
X = df[["Advertising", "Visitors"]]  # Features / inputs
y = df["Sales"]                      # Target / output

# 2. SPLIT DATA
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 3. CREATE AND TRAIN MODEL
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# 4. PREDICT
predictions = model.predict(X_test)

# KEY TERMS
# Algorithm  = method used to learn patterns
# Model      = result after learning from training data
# Features   = input variables (X)
# Target     = value being predicted (y)
# Training   = learning patterns from training data
# Testing    = evaluating on held-out data
# Prediction = model's estimated output

# TYPES OF MACHINE LEARNING
# Supervised    = learns from labelled examples
# Unsupervised  = finds patterns without target labels
# Reinforcement = learns actions from rewards/penalties

# REMEMBER
# Keep test data separate from training.
# Predictions are not necessarily accurate.
# Correlation does not prove causation.
# Always evaluate a model before trusting it.
