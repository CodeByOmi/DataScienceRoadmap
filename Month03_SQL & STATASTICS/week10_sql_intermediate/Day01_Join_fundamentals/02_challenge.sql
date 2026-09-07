select m.name,m.age,m.city,ms.Membership,ms.Monthly_Fee
from members as m
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where m.age > 25 
and ms.membership = 'VIP'
ORDER BY ms.Monthly_Fee desc;