--1 CTE

with heavy_members as (
SELECT name, Weight_kg
from members
where Weight_kg > 80
)
select * 
from heavy_members;




--2 cte  + aggregation

with average_weight as (
select avg(Weight_kg) as avg_weight
from members
)
select m.name,m.Weight_kg
from members as m 
WHERE m.Weight_kg >(
select avg_weight 
from average_weight
);




--3 cte + join

with adult_members as (
select *
from members
where age > 25
)
SELECT am.name,am.age,ms.Membership,ms.Monthly_Fee
from adult_members as am
inner join memberships as ms 
on am.Membership_ID = ms.Membership_ID;




--4 CTE + group by

WITH city_members AS (
SELECT city,
COUNT(*) AS member_count
FROM members
GROUP BY city
)
SELECT *
FROM city_members
ORDER BY member_count DESC;


with city_stats as (
select city,
avg(age) as average_age
from members
group by city
)
select city,average_age
from city_stats
order by average_age desc;




--5 multiple CTEs

with older_members as (
SELECT * 
from members 
where age >= 25),
vip_members as (
select * 
from members
where Membership_ID = '103')
select * 
from vip_members;




--6 CTE + JOIN + GROUP BY

with member_info as (
select m.name,ms.Membership,ms.Monthly_Fee
from members as m
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
)

SELECT membership,
count(*) as member_count
from member_info
group by membership 
order by member_count desc;


