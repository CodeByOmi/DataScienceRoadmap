SELECT m.name,m.age,ms.membership,ms.monthly_fee,t.trainer_name,t.specialization
from members as m 
inner join memberships as ms
on m.membership_id = ms.membership_id
left join member_trainers as mt 
on m.member_id = mt.member_id
left join trainers as t 
on mt.trainer_id = t.trainer_id
where m.age >= 25
order by monthly_fee desc;
