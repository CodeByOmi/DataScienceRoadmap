--1 row()number

select name,Weight_kg,
row_number() over(order by Weight_kg desc) as weight_rank
from members;

select name,age,
row_number() over(order by age desc) as age_rank
from members;


--2 rank

select name,Weight_kg,
rank() over(order by Weight_kg desc) as weight_rank
from members;


select name,age,
rank() over(order by age desc) as age_rank
from members;


--3 dense rank

select name,age,
dense_rank() over(order by age desc) as age_rank
from members;

SELECT name,Height_cm,
dense_rank() over(order by Height_cm desc) as height_rank
from members;


-- partition by and rank

select name,Membership_ID,Weight_kg,
rank() over(PARTITION by Membership_ID 
order by Weight_kg desc) as membership_rank
from members;


-- top n 

with ranked_members as (
SELECT name,Weight_kg,
row_number() over(order by Weight_kg desc)
as Weight_rank
FROM members)

SELECT name,Weight_kg
from ranked_members
where weight_rank <=5;


--ranking by business metrics

SELECT member_id,Payment_Date,Amount,
row_number() over(order by Amount desc) as payment_rank
from payments;


