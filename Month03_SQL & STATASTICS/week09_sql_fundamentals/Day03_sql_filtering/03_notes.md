SQL DAY 3 — FILTERING & HAVING

IN
→ check multiple possible values

WHERE City IN ('Pune', 'Mumbai');

BETWEEN
→ filter a range

WHERE Age BETWEEN 20 AND 30;

LIKE
→ text pattern matching

'A%'    → starts with A
'%a'    → ends with a
'%an%'  → contains an

HAVING
→ filter grouped results

SELECT City, COUNT(*) AS members
FROM gym_members
GROUP BY City
HAVING COUNT(*) > 5;

WHERE
→ filters rows

HAVING
→ filters groups

Important order:

WHERE
↓
GROUP BY
↓
HAVING
↓
ORDER BY