--1 basic queris

SELECT name,age,city
from gym_members;

select Name,age,Weight_kg
from gym_members
where age > 25
and Weight_kg > 70;

SELECT name,Age
from gym_members
ORDER by age asc;



--2 filtering

select name , membership
from gym_members
where Membership in ('VIP','Basic');


SELECT name,age,City
from gym_members
where age BETWEEN 20 and 30
and city = 'Pune';


SELECT Name
from gym_members 
where name like '%a';


--3 aggregation

SELECT
count(name) as total_members,
avg(Weight_kg) as average_weight,
avg(age) as average_age
from gym_members;


select 
sum(Weight_kg) as total_weight
from gym_members;

select 
min(age) as minimum_age,
max(age) as maximum_age
from gym_members;



--4 group by

select city,
count(*) as members
from gym_members
group by city;

SELECT Membership,
avg(Weight_kg) as average_weight
from gym_members
group by Membership;

SELECT city,
count(*) as members,
avg(age) as average_age,
avg(Weight_kg) as average_weight
from gym_members
group by city;




--5 having

SELECT Membership,
count(*) as members
from gym_members
GROUP by Membership
having members > 5;

select city,
avg(Weight_kg) as average_weight
from gym_members
group by Membership
having average_weight > 70;



--6 null

select name
from gym_members
where age is null;

SELECT name,Weight_kg
from gym_members
where Weight_kg is not null;




--7 case

select name,Weight_kg,
CASE
when Weight_kg < 60 then 'light'
when Weight_kg < 75 then 'normal'
else 'heavy'
end as weight_category
from gym_members;



select name,age,
CASE
when age < 25 then 'young'
when age < 35 then 'adult'
else 'senior'
end as age_category
from gym_members;


--8 real problems

SELECT Membership,
count(*) as members
from gym_members
group by Membership
order by members desc;


SELECT City,
count(*) as members,
avg(age) as average_age
from gym_members
GROUP by city 
having members > 5
and average_age > 28
ORDER by members desc;



--final challenge 

SELECT 
case 
when age < 25 then 'young'
when age < 35 then 'adult'
else 'senior'
end as age_category,
count(*) as members,
avg(age) as average_age,
max(Weight_kg) as maximum_weight
from gym_members
where age BETWEEN 20 and 40
and city in ('Pune','Mumbai','Nashik')
GROUP by
CASE
when age < 25 then 'young'
when age < 35 then 'adult'
else 'senior'
end
HAVING members >= 3
ORDER by members desc;
