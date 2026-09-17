WINDOW FUNCTIONS

Window functions perform calculations
without collapsing individual rows.

Basic syntax:

function() OVER()


Example:

AVG(age) OVER()


PARTITION BY

Creates separate windows for calculations
while keeping individual rows.

Example:

AVG(age) OVER(
    PARTITION BY membership_id
)


Common window functions:

AVG() OVER()
SUM() OVER()
COUNT() OVER()
MAX() OVER()
MIN() OVER()


GROUP BY:
Combines rows into groups.

Window function:
Keeps individual rows and adds calculations.


Example:

SUM(amount) OVER(
    PARTITION BY member_id
)

= total amount for each member,
while keeping every payment row.