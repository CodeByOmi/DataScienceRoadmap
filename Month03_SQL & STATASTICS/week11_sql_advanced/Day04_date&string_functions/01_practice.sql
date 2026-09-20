--1 data function

select Payment_Date,
strftime('%Y', Payment_Date) as year,
strftime('%m', Payment_Date) as month,
strftime('%d', Payment_Date) as day
from payments;



--2 grouping by month

select strftime('%m', payment_date) as month,
sum(amount) as total_amount
from payments
group by month
order by month;



--3 year + month

select strftime('%Y-%m' , payment_date) as month,
sum(amount) as total_payments
from payments
group by month
order by month;



--4 string function

SELECT name, 
upper(name) as upper_case,
lower(name) as lower_case,
length(name) as length_name
from members;



--5 substr

select name, substr(name,1,1) as first_letter
from members;




--6 Combine Advanced SQL + Dates + Strings

--For each month, calculate the total payment collected and 
--rank the months from highest payment to lowest payment.


select strftime('%Y-%m', Payment_Date) as Month,
sum(amount) as total_payments,
rank() over(order by sum(amount) desc) as payment_rank
from payments
group by month;

