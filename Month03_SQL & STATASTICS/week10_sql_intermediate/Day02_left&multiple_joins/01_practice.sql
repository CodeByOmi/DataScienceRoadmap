--1 left join

SELECT m.name,p.payment_status
from members as m 
left join payments as p 
on m.Member_ID = p.Member_ID;




--2 left join + where

SELECT m.name,p.Payment_Date,p.Amount,p.Payment_Status
from members as m 
left join payments as p 
on m.Member_ID = p.Member_ID
where amount > 2000;



--3 joining 3 tabels

select m.name,ms.Membership,p.Amount,p.Payment_Status
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
inner join payments as p
on m.Member_ID = p.Member_ID
where p.amount > 2000;


--4 multiple joins

SELECT m.name,ms.Membership,ms.Monthly_Fee,p.Amount,p.Payment_Status
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
left join payments as p 
on m.Member_ID = p.Member_ID;



--5 bridge table

SELECT m.name,t.Trainer_Name,t.Specialization
from members as m
inner join member_trainers as mt 
on m.Member_ID = mt.Member_ID
inner join trainers as t 
on mt.Trainer_ID = t.Trainer_ID;


--6 all combine

SELECT m.name,m.age,ms.Membership,ms.Monthly_Fee
from members as m 
inner join memberships as ms 
on m.Membership_ID = ms.Membership_ID
where m.age >= 25
order by Monthly_Fee desc;