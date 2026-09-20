SELECT Payment_Date,amount,
sum(amount) over(order by Payment_Date) as running_total
from payments;


SELECT Payment_ID,
       Payment_Date,
       Amount,
       SUM(Amount) OVER(
           ORDER BY Payment_Date, Payment_ID
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM payments;


SELECT name,Weight_kg,
rank() over(order by Weight_kg desc) as weight_rank
from members;


SELECT m.name,ms.Membership,m.Weight_kg,
rank() over(PARTITION by ms.Membership
order by m.Weight_kg desc) as weight_rank
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID;


SELECT member_id,Payment_Date,amount,
lag(Amount) over(PARTITION by Member_ID
order by Payment_Date) as previous_payment
from payments;


SELECT strftime('%m',payment_date) as Month ,
sum(Amount) as total_payments,
dense_rank() over(order by sum(Amount) desc) as payment_rank
from payments
group by month 
order by total_payments desc ;




SELECT ms.membership,
sum(p.amount) as total_payment,
rank() OVER(order by sum(p.amount) desc ) as payment_rank
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
inner join payments as p 
on m.Member_ID = p.Member_ID
group by ms.Membership
order by payment_rank ;


