-- Business question
-- For each membership type, find the top 3 heaviest members.



with ranked_member as (
SELECT m.name,m.Weight_kg,ms.Membership,
rank() over(partition by ms.Membership_ID
order by m.Weight_kg desc) as weight_rank
from members as m 
inner join memberships as ms 
on m.membership_ID = ms.membership_id)

select name,Weight_kg,membership
from ranked_member
where weight_rank <= 3;
