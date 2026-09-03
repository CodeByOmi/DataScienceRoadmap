--1 column allises

select 
name as member_name,
Age as membera_age
from gym_members;

select name,Weight_kg,
Weight_kg * 2.20462 as weight_lbs
from gym_members;



--2 combining IN, BETWEEN, LIKE

SELECT *
from gym_members
where name like 'R%'
and age > 25;

select *
from gym_members
where Name LIKE '%a%'
and city = 'Mumbai';

SELECT *
FROM gym_members
WHERE City IN ('Pune', 'Mumbai')
AND Age BETWEEN 20 AND 30;




--3 null handling

SELECT *
from gym_members
where age is null;

select *
from gym_members 
WHERE city is not null;




--5  case when

select name,age,
CASE
when age < 25 then 'Young'
when age < 35 then 'Adult'
else 'Senior'
end as Age_group
from gym_members;

select name,Weight_kg,
CASE
when Weight_kg < 60 THEN 'Light'
when Weight_kg < 75 then 'Normal'
else 'Heavy'
end as weight_category
from gym_members;




-- case + aggregate analysis

SELECT 
case 
when age < 25 then 'Young'
when age < 35 THEN 'Adult'
else 'senior'
end as age_group,
count(*) as member
from gym_members
group BY
CASE
when age < 25 then 'Young'
when age < 35 THEN 'Adult'
else 'senior'
end;



select 
CASE
when Weight_kg < 60 then 'light'
when Weight_kg < 75 then 'normal'
else 'heavy'
end as weight_category,
count(*) as member 
from gym_members
GROUP BY
case
when Weight_kg < 60 then 'light'
when Weight_kg < 75 then 'normal'
else 'heavy'
end;



SELECT
    CASE
        WHEN Age < 25 THEN 'Young'
        WHEN Age <= 35 THEN 'Adult'
        ELSE 'Senior'
    END AS age_category,
    AVG(Weight_kg) AS average_weight
FROM gym_members
GROUP BY
    CASE
        WHEN Age < 25 THEN 'Young'
        WHEN Age <= 35 THEN 'Adult'
        ELSE 'Senior'
    END;