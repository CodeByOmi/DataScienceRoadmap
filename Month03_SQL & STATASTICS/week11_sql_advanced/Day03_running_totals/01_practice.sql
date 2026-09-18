-- running totals

SELECT payment_date,Amount,
sum(amount) over(order by Payment_Date) as running_total
from payments;



--per member

SELECT member_id,Payment_Date,amount,
sum(amount) over(partition by Member_ID
order by Payment_Date ) as running_total
from payments;



--lag

SELECT Payment_Date,Amount,
lag(amount) over(order by Payment_Date) as previous_payment
from payments;



-- change previous row

SELECT Payment_Date,amount,
lag(amount) over(order by Payment_Date)
as previous_amount,
amount - lag(Amount) over (order by Payment_Date) 
as change_amount
from payments;



-- lead

SELECT Payment_Date,amount,
lead(amount) over(PARTITION by Member_ID
order by Payment_Date)
as next_amount
from payments;