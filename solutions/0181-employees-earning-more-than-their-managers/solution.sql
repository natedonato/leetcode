# Write your MySQL query statement below

SELECT E1.name AS Employee FROM employee E1 JOIN employee E2 on E1.managerID = E2.id WHERE E1.salary > E2.salary 
