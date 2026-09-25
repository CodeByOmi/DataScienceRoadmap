CONDITIONAL:
P(A|B) = P(A∩B) / P(B)

INDEPENDENCE:
P(A∩B) = P(A) × P(B)

BAYES:
P(H|E) = P(E|H) × P(H) / P(E)

DISTRIBUTIONS:
Discrete → countable
Continuous → measurable
Binomial → np.random.binomial(n,p,size)
Normal → np.random.normal(mean,std,size)

HYPOTHESIS:
H₀ → no difference/effect
H₁ → difference/effect

p < 0.05  → Reject H₀
p ≥ 0.05 → Fail to reject H₀

T-TEST:
ttest_1samp(data, mean)

KEY:
Prior → before evidence
Likelihood → P(E|H)
Evidence → P(E)
Posterior → P(H|E)