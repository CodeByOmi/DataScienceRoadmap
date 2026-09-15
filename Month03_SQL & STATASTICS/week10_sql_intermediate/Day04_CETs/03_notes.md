CTE = Common Table Expression

A CTE creates a temporary result
that can be used by the main query.

Basic syntax:

WITH cte_name AS (
    SELECT ...
    FROM ...
)
SELECT *
FROM cte_name;


CTE + WHERE:

WITH older_members AS (
    SELECT *
    FROM members
    WHERE age >= 25
)
SELECT *
FROM older_members;


CTE + JOIN:

WITH older_members AS (
    SELECT *
    FROM members
    WHERE age >= 25
)
SELECT ...
FROM older_members AS o
INNER JOIN memberships AS ms
ON o.membership_id = ms.membership_id;


Multiple CTEs:

WITH cte1 AS (
    ...
),
cte2 AS (
    ...
)
SELECT ...


CTE can be combined with:
- JOIN
- WHERE
- GROUP BY
- AVG()
- COUNT()
- ORDER BY

Main benefit:
Break complicated SQL into clear steps.