WINDOW FUNCTIONS
────────────────────────────────

SUM() OVER()
→ window total

SUM() OVER(
    ORDER BY date
)
→ running total

ROW_NUMBER()
→ unique ranking number

RANK()
→ ranking with gaps

DENSE_RANK()
→ ranking without gaps

LAG()
→ previous row

LEAD()
→ next row

PARTITION BY
→ restart calculation for each group

ORDER BY
→ determines the order inside the window


DATES
────────────────────────────────

strftime('%Y', date)
→ year

strftime('%m', date)
→ month

strftime('%d', date)
→ day

strftime('%Y-%m', date)
→ year-month


STRINGS
────────────────────────────────

UPPER(name)
LOWER(name)
LENGTH(name)
SUBSTR(name, start, length)


ADVANCED PATTERN
────────────────────────────────

JOIN
 ↓
GROUP BY
 ↓
SUM / AVG / COUNT
 ↓
Window function
 ↓
ORDER BY