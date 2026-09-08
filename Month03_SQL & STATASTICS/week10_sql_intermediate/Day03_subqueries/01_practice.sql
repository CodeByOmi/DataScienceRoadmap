--1 subquery

SELECT name,Weight_kg
from members
where Weight_kg > (
SELECT avg(Weight_kg)
from members);


--2 subquery with in

SELECT name, membership_id
FROM members 
WHERE membership_id IN (
    SELECT membership_id
    FROM memberships
    WHERE monthly_fee <1500 
);

SELECT name , Membership_ID
from members
where Membership_ID in (
select Membership_ID
from memberships
where Monthly_Fee >= 2000
);




--3 max min

SELECT name,Weight_kg
from members
where Weight_kg = (
SELECT max(Weight_kg)
from members); 




--4 from

SELECT * 
from(
select name,age,Weight_kg
from members
) as x
where age >= 25;



--5 correlated
select m.name,m.gender,m.Weight_kg
from members as m 
where m.Weight_kg > (
SELECT avg(m2.Weight_kg)
from members as m2 
where m.Gender = m2.Gender
);


--6 with join 

SELECT m.name,ms.Membership,ms.Monthly_Fee
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where Monthly_Fee = (
SELECT max(Monthly_Fee)
from memberships
);