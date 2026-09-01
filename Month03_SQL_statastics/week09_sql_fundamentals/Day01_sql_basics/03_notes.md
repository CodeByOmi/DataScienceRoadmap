SQL DAY 1

SELECT
→ choose columns

SELECT *
FROM table;

SELECT Name, Age
FROM table;

DISTINCT
→ unique values

SELECT DISTINCT City
FROM table;

WHERE
→ filter rows

WHERE Age > 25

Operators:
=   <>   >   <   >=   <=

AND
→ both conditions

OR
→ either condition

NOT
→ reverse condition

ORDER BY
→ sort

ORDER BY Age ASC
ORDER BY Weight_kg DESC

LIMIT
→ number of rows

LIMIT 5

Common pattern:

SELECT columns
FROM table
WHERE condition
ORDER BY column DESC
LIMIT 5;