--1 aggregate fuctions

SELECT  count(Name)
from gym_members;

SELECT sum(Weight_kg) as total_sum
from gym_members;


SELECT avg(Age) as average_age
FROM gym_members;


select count(City)
FROM gym_members;


SELECT max(Weight_kg)
FROM gym_members;



--2 multiple aggregate fuction

select 
count(*) as  Total_members,
avg(Age) as  Average_age,
max(Weight_kg) as maximum_weight,
min(Weight_kg) as minimum_weight
from gym_members;




--3 group by

select
Membership,
count(*) as total_members
from gym_members
group by membership;


SELECT
city,
count(*) as total_city_members
FROM gym_members
group by city;

select 
Membership,
min(age) as min_age
From gym_members
GROUP by Membership;


select 
city,
max(Weight_kg) as max_weight
from gym_members
GROUP by city;


--4 group by and multiple aggregation

SELECT 
City,
count(*) as total_members,
avg(age) as average_age,
min(Weight_kg) as min_weight
from gym_members
group by city;



--5 group by + order by

SELECT
Membership,
COUNT(*) AS members
FROM gym_members
GROUP BY Membership
ORDER BY members desc;


SELECT 
City,
avg(age) as average_age,
count(*) as members
from gym_members
group by city
order by members asc;
