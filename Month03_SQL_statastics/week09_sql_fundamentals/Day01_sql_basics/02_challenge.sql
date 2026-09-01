SELECT Name,Age,Weight_kg,City,Membership
from gym_members
where membership = 'VIP'
and Age >= 25
and Weight_kg  > 70 
ORDER by weight_kg desc
limit 5;