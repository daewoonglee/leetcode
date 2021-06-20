"""
select name as Employee from employee as e
where e.salary > (select salary from employee where e.ManagerId = Id)

select a.name as Employee from Employee as a join employee as b
on a.ManagerId = b.Id and a.Salary > b.Salary
"""