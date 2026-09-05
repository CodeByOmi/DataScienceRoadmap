SQL DAY 2 — AGGREGATION

Aggregate functions:
COUNT() → count
SUM()   → total
AVG()   → average
MIN()   → smallest
MAX()   → largest

AS
→ gives a result a temporary name

GROUP BY
→ creates groups of similar values

Example:

SELECT City, COUNT(*)
FROM gym_members
GROUP BY City;

Multiple aggregates:

SELECT
    City,
    COUNT(*) AS members,
    AVG(Age) AS average_age
FROM gym_members
GROUP BY City;

Multiple groups:

GROUP BY City, Membership

Sort grouped results:

ORDER BY members DESC

Common pattern:

SELECT group_column,
       COUNT(*) AS count,
       AVG(column) AS average
FROM table
GROUP BY group_column
ORDER BY count DESC;