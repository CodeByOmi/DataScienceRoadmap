RANKING WINDOW FUNCTIONS

ROW_NUMBER()
→ Gives every row a unique number.
→ Ties do NOT share a number.

RANK()
→ Ties get the same rank.
→ Gaps appear after ties.

DENSE_RANK()
→ Ties get the same rank.
→ No gaps after ties.


Basic:

ROW_NUMBER() OVER(
    ORDER BY column DESC
)

RANK() OVER(
    ORDER BY column DESC
)

DENSE_RANK() OVER(
    ORDER BY column DESC
)


Partitioned ranking:

RANK() OVER(
    PARTITION BY group_column
    ORDER BY value_column DESC
)


Top N:

WITH ranked AS (
    SELECT ...,
           ROW_NUMBER() OVER(
               ORDER BY column DESC
           ) AS rank_num
    FROM table
)
SELECT *
FROM ranked
WHERE rank_num <= N;