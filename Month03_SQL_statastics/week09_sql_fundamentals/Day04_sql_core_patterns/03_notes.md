SQL DAY 4 — CORE QUERY PATTERNS

AS
→ rename output columns

IN
→ match multiple values

BETWEEN
→ filter a range

LIKE
→ text pattern matching

IS NULL
→ find missing values

IS NOT NULL
→ find non-missing values

CASE
→ create categories based on conditions

Basic CASE:

CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END AS column_name

SQL query order:

SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

WHERE
→ filters rows

HAVING
→ filters groups

CASE + GROUP BY
→ categorize data and analyze each category