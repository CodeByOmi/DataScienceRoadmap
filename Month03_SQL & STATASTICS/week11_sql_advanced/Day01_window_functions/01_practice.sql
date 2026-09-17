--1 over

select name,age,
avg(age) over() as average_age
from members;



-- partition by

select name,Membership_ID,age,
avg(age) over( PARTITION by Membership_ID ) as average_age_by_membership
from members;



-- sum over

select m.name,p.amount,
sum(amount) over() as total_payment
from members as m 
inner join payments as p;



-- sum + partition by

select member_id,Payment_Date,Amount,
sum(amount) over(PARTITION by Member_ID) as member_total
from payments;


-- count over

SELECT name,city,
COUNT(*) OVER() AS total_members
FROM members;

SELECT name,city,
COUNT(*) OVER(PARTITION BY city)
AS city_member_count
FROM members;



