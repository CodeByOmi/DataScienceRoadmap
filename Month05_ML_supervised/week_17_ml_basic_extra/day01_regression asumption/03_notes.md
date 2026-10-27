# Week 17 Day 1 — Regression Assumptions

## Residuals
Residual = Actual - Predicted

Positive residual: underprediction
Negative residual: overprediction

## 1. Linearity
Check residual plots for curved patterns.
Possible response: transform features or add polynomial features.

## 2. Independence
Errors should not be systematically related.
For time series, inspect residuals over time and autocorrelation.

## 3. Constant variance
Homoscedasticity: roughly constant error variance.
Heteroscedasticity: changing error variance.
Check residual spread against predictions.

## 4. Multicollinearity
Strong linear relationships among features can destabilize
individual coefficients.
Check feature correlations and consider VIF.

## 5. Normality of errors
Primarily relevant to traditional statistical inference,
especially in small samples.
Inspect residual histograms and Q-Q plots.

## Important
Diagnostic plots reveal clues, not absolute proof.
Assumption violations do not automatically make predictions useless.
Use held-out data or cross-validation for model evaluation.