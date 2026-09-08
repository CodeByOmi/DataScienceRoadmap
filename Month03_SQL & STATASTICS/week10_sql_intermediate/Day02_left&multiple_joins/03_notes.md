# Week 10 Day 2 — LEFT JOIN + Multiple JOINs

## LEFT JOIN

LEFT JOIN keeps ALL rows from the left table.

Syntax:

SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;

If no match exists:
SQL returns NULL for columns from the right table.

## INNER JOIN vs LEFT JOIN

INNER JOIN:
Only matching rows.

LEFT JOIN:
All rows from left table + matching rows from right table.

## Multiple JOINs

We can join more than two tables.

FROM table1
JOIN table2
ON ...
JOIN table3
ON ...

## Bridge / Junction Table

A middle table can connect two tables.

Example:

members
   ↓
member_trainers
   ↓
trainers

## JOIN + WHERE

FROM ...
JOIN ...
ON ...
WHERE condition;

## JOIN + ORDER BY

FROM ...
JOIN ...
ON ...
WHERE ...
ORDER BY column DESC;

## Important

ON → tells SQL how tables connect

WHERE → filters rows

ORDER BY → sorts results

LEFT JOIN → keeps all rows from left table

NULL → missing matching information