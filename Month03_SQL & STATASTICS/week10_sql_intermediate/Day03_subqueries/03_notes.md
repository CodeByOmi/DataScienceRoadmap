# week 10 day 3 SUBQUERY

A subquery is a query inside another SQL query.

Basic:
SELECT ...
FROM members
WHERE age > (
    SELECT AVG(age)
    FROM members
);

IN:
WHERE membership_id IN (
    SELECT membership_id
    FROM memberships
    WHERE monthly_fee > 1500
);

MAX/MIN:
WHERE monthly_fee = (
    SELECT MAX(monthly_fee)
    FROM memberships
);

Subquery in FROM:
SELECT *
FROM (
    SELECT ...
    FROM members
) AS x;

Correlated subquery:
A subquery that depends on the current row
of the outer query.

Subqueries are useful for:
- comparing with averages
- finding maximum/minimum
- filtering using another table
- solving multi-step SQL problems