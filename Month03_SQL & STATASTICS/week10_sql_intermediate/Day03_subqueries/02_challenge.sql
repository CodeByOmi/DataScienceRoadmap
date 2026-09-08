--Find all members who are older than the average member 
-- age AND belong to a membership whose fee is greater 
-- than ₹1500.


SELECT m.name,m.age,ms.membership,ms.Monthly_Fee
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where m.age > (
SELECT avg(age)
from members as m2
)
-- and ms.Monthly_Fee > 1500
-- or using in 

and m.Membership_ID in (
select Membership_ID
from memberships
where Monthly_Fee > 1500
)
order by age desc;

