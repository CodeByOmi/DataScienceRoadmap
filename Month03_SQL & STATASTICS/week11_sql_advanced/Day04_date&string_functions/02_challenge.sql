-- Business problem

-- Management wants to understand which membership type 
-- generates the most payment revenue.


SELECT ms.membership,
sum(p.amount) as total_payment,
rank() OVER(order by sum(p.amount) desc) as payment_rank
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
inner join payments as p 
on m.Member_ID = p.Member_ID
group by ms.Membership
order by payment_rank;
