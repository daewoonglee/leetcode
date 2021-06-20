"""
select name as Customers from customers as c
where c.id not in (select CustomerId from Orders)

select name as Customers
from customers as c left join Orders as o
on c.Id = o.customerId
where o.customerId is NULL
"""