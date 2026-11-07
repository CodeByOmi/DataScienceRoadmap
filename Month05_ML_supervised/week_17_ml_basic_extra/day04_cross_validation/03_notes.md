# Week 17 — Day 4: Cross-Validation & Model Selection

## 1. Cross-Validation
Evaluates a model using multiple training and validation splits.

## 2. K-Fold
Divides data into K parts. Each part gets one turn as validation data.

## 3. cross_val_score()
Evaluates a model across multiple folds.

## 4. Mean and Standard Deviation
- Mean: Average model performance.
- Standard deviation: Measures score variation across folds.

## 5. Model Comparison
Compare algorithms using the same cross-validation splits.

## 6. Model Selection
Choose a suitable model based on performance, consistency, and generalization.

## Important Tools
- `KFold()` — creates cross-validation splits.
- `cross_val_score()` — evaluates models.
- `.mean()` — calculates average.
- `.std()` — calculates standard deviation.
- `LinearRegression()` — linear regression model.
- `DecisionTreeRegressor()` — tree-based regression.
- `RandomForestRegressor()` — ensemble of decision trees.
- `train_test_split()` — separates training and test data.

## Important Rule
Use cross-validation during model selection.
Keep the test set separate for final evaluation.