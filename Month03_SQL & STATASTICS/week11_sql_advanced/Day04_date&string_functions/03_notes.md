## WEEK 11 — DAY 4

DATE FUNCTIONS

Extract year:
strftime('%Y', payment_date)

Extract month:
strftime('%m', payment_date)

Extract day:
strftime('%d', payment_date)

Year + month:
strftime('%Y-%m', payment_date)


STRING FUNCTIONS

Uppercase:
UPPER(name)

Lowercase:
LOWER(name)

Character count:
LENGTH(name)

Part of string:
SUBSTR(name, start, length)


IMPORTANT PATTERN

Aggregate first → Window function

Example:

GROUP BY month
SUM(amount)

then:

RANK() OVER(
    ORDER BY SUM(amount) DESC
)


Relationships:

members → payments
Member_ID

members → memberships
Membership_ID