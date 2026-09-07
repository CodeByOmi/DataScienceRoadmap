--1

SELECT name,Membership_ID
from members;

select Membership_ID,Monthly_Fee
from memberships;


--2 inner join

SELECT members.name,memberships.membership,memberships.Monthly_Fee
from members
inner JOIN memberships
on members.Membership_ID = memberships.Membership_ID;



--3 table alises

select m.name,ms.Membership,ms.Monthly_Fee
from members as m
inner join memberships as ms
on m.Membership_ID = ms.Membership_ID;



--4 join + where

SELECT m.name,ms.membership,ms.Monthly_Fee
from members as m
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where ms.Monthly_Fee < 2000;


--5  join + oreder by

SELECT m.name,ms.membership,ms.Monthly_Fee
from members as m
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
order by ms.Monthly_Fee asc;


select m.name,m.age,m.city,m.Membership,ms.Monthly_Fee
from members as m
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where m.age > 25 
and ms.membership = 'VIP'
ORDER BY ms.Monthly_Fee desc;