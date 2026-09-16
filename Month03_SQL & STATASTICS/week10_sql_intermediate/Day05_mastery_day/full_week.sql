--1 

select m.name,ms.Membership
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID;



--2

select m.name,p.Payment_Date,p.Amount
from members as m 
left join payments as p 
on m.Member_ID = p.Member_ID;


--3

select m.name,ms.membership,t.Trainer_Name
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
inner join member_trainers as mt 
on m.Member_ID = mt.Member_ID
inner join trainers as t
on t.trainer_ID = mt.trainer_id;



--4 

select m.name,m.age,ms.Membership,ms.Monthly_Fee
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where m.age >= 25
order by ms.Monthly_Fee desc;


--5 

SELECT name,Age
from members 
where age > (
select avg(age)
from members);



--6

SELECT name,Membership_ID
from members
where Membership_id in(
SELECT Membership_ID
from memberships 
where Monthly_Fee > 1500
);



--7 

with older_members as (
SELECT *
from members
where age >= 25
)
SELECT om.name,om.age,ms.Membership,ms.Monthly_Fee
from older_members as om
inner join memberships as ms 
on om.Membership_ID = ms.Membership_ID;



--8

with city_members as (
SELECT city,
count(*) as member_count
from members 
group by City
)
SELECT * 
from city_members 
order by member_count desc;


--9

select m.name,ms.Membership,ms.Monthly_Fee
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where Monthly_Fee = (
SELECT max(Monthly_Fee)
from memberships );


--10 

with members_class as (
select m.name,m.age,ms.membership
from members as m 
inner join memberships as ms
on m.membership_id = ms.membership_id
where m.age >= 25
)
select Membership,
avg(age) as average_age
from members_class
group by membership 
order by average_age desc;