-- The manager asks:
-- I want a report for each city showing the number of 
-- members, average age, and average weight. 
-- Show the cities with the most members first.

SELECT
city,
count(*) as members,
avg(age) as average_age,
avg(weight_kg) as average_weight
from gym_members
group by city
order by members desc;
