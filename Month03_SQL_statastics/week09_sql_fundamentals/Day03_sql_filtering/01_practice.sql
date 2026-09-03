--1 IN

SELECT name,Membership
from gym_members
WHERE Membership IN ('VIP', 'Premium');

select name,city
FROM gym_members
WHERE city in ('Mumbai','Pune','Thane');




--2 BETWEEN

select *
from gym_members
where age between 20 and 30;

select *
from gym_members
where Weight_kg between 75 and 85;



--3 LIKE

select *
from gym_members
where name like '%an%';

select * 
FROM gym_members
where name like 's%';

select * 
FROM gym_members
where city like 'M%';


--4 HAVING

select Membership,
count(*) as Member
from gym_members
group by membership
HAVING count(*) > 15;

select city,
avg(age) as average_age
from gym_members
group by City
having avg(age) > 25;


select Membership,
avg(Weight_kg) as average_weight
from gym_members
group by Membership
having avg(Weight_kg) > 70;



--5 WHERE + GROUP BY + HAVING

select city,
avg(Weight_kg) as average_weight
from gym_members
where age > 25
group by City;

select city,
count(*) as Members
from gym_members
where Weight_kg >70
group by City
having count(*) >=3;
