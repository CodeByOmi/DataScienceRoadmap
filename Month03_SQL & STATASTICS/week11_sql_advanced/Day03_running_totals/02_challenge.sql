-- Business question:

-- For every member, show their payment history with:

-- member_id
-- payment_date
-- amount
-- running total of their payments
-- previous payment amount
-- difference between current and previous payment


select Member_ID,payment_date,Amount,
sum(amount) over(PARTITION by Member_ID
order by payment_date) as running_total,
lag(amount) over(PARTITION by Member_ID
order by Payment_Date) as prvious_amount,
amount - lag(amount) over(partition by Member_ID
order by Payment_Date) as differnce_in_amount  
from payments;