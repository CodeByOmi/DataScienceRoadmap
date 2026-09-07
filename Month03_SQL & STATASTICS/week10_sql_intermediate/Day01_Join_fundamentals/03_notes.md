# Week 10 Day 1 — JOIN Fundamentals

## JOIN
JOIN combines related data from multiple tables.

## Primary Key
Uniquely identifies each row.

Example:
Member_ID

## Foreign Key
Connects a row to another table.

Example:
Membership_ID

## INNER JOIN

SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;

INNER JOIN returns matching rows from both tables.

## Table Aliases

FROM members AS m
INNER JOIN memberships AS ms

m = members
ms = memberships

## JOIN + WHERE

SELECT ...
FROM table1
INNER JOIN table2
ON ...
WHERE condition;

## JOIN + ORDER BY

SELECT ...
FROM table1
INNER JOIN table2
ON ...
ORDER BY column DESC;

## Important

ON → connects tables

WHERE → filters rows

ORDER BY → sorts results

ASC → low to high

DESC → high to low