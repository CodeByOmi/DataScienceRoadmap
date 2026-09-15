-- Find the average age of members for each membership type,
-- but only include members whose age is 25 or older.


with members_class as (
select m.name,m.age,ms.membership
from members as m 
inner join memberships as ms
on m.membership_id = ms.membership_id
where m.age >= 25
)
select Membership,
avg(age) as average_age
from members_class
group by membership 
order by average_age desc;
