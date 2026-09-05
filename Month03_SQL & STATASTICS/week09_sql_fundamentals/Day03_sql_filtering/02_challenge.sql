--The manager asks:

-- "For members aged between 20 and 30, 
-- show each membership type and the number of members. 
-- Only show membership types having at least 7 members, and 
-- show the largest groups first."

select membership,
count(*) as members
from gym_members
where age between 20 and 30
group by  membership
HAVING count(*) >= 7
order by members DESC;
