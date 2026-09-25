# Week 13 Day 4 — Hypothesis Testing

Population:
Entire group.

Sample:
Smaller group taken from population.

H₀ (Null Hypothesis):
Usually represents no difference/no effect.

H₁ (Alternative Hypothesis):
What we want to investigate against H₀.

α (Significance Level):
Decision threshold.
Common value = 0.05

p-value:
How unusual the observed data is under H₀.

Decision:
p-value < α
→ Reject H₀

p-value >= α
→ Fail to reject H₀

Important:
Fail to reject H₀ does NOT prove H₀ is true.

Type I Error:
Reject a true H₀.
False alarm.

Type II Error:
Fail to reject a false H₀.
Miss.

Python:
from scipy.stats import ttest_1samp

result = ttest_1samp(sample, population_mean)

result.statistic
result.pvalue