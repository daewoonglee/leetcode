"""
SELECT MAX(salary) as SecondHighestSalary FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)

SELECT
    (SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary
"""