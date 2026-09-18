## WEEK 11 — DAY 3

Running total:
SUM(amount) OVER(
    ORDER BY payment_date
)

Running total per group:
SUM(amount) OVER(
    PARTITION BY member_id
    ORDER BY payment_date
)

LAG = previous row:
LAG(amount) OVER(
    ORDER BY payment_date
)

LEAD = next row:
LEAD(amount) OVER(
    ORDER BY payment_date
)

Previous value per member:
LAG(amount) OVER(
    PARTITION BY member_id
    ORDER BY payment_date
)

Change from previous:
amount - LAG(amount) OVER(
    ORDER BY payment_date
)

Remember:
LAG()  → previous
LEAD() → next
PARTITION BY → separate calculation for each group
ORDER BY → defines row sequence