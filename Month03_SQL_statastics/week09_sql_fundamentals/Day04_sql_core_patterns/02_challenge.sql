--The manager asks:

--"Analyze members aged between 20 and 40 from 
-- Pune, Mumbai, or Nashik. Categorize them into Young, 
-- Adult, and Senior based on age. Show the number of 
-- members in each age category and their average weight.
--  Only show categories with at least 2 members, 
--  and put the category with the most members first."


select 
CASE
when age < 25  then 'Young'
when age < 35 then 'Adult'
else'Senior'
end as Age_category,
count(*) as members,
avg(weight_kg) as average_weight
from gym_members
where age between 20 and 40 
and city in ('Pune','Mumbai','Nashik')
group BY
case 
when age < 25 then 'Young'
when age < 35 then 'Adult'
else 'Senior'
END
having count(*) >= 2
order by members desc;

