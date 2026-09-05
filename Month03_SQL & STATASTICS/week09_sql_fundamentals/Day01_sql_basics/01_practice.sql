--1 select

SELECT * 
FROM gym_members;

SELECT Name,Age,City
FROM gym_members;



--2 distinct

SELECT DISTINCT Membership
FROM gym_members;

select DISTINCT City,Membership
from gym_members;



--3 where

SELECT *
FROM gym_members
WHERE Age > 30;

SELECT * 
from gym_members
where Weight_kg <= 70;


SELECT *
FROM gym_members
WHERE Membership <> 'Basic';



--4 and, or, not


SELECT *
from gym_members
WHERE Age > 25 
and Weight_kg > 80;


select * 
from gym_members
where not Membership = 'Basic'
and age >= 30;


SELECT *
from gym_members
where City = 'Mumbai'
or city = 'Pune';



--5 order by

select *
from gym_members
order by age asc;

select * 
from gym_members
order by Membership asc , Weight_kg desc;



--6  LIMIT

SELECT *
FROM gym_members
order by Age ASC
LIMIT 3;



select *
from gym_members
order by weight_kg DESC
limit 8;

