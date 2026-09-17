SELECT name,age,Membership_ID,city,
avg(age) over(PARTITION by Membership_ID) as membership_avg_age,
count(*) over(PARTITION by city) as city_members_count
from members;