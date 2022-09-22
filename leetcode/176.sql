-- Write your MySQL query statement below

-- +-------------+------+
--| Column Name | Type |
--+-------------+------+
--| id          | int  |
--| salary      | int  |
--+-------------+------+
--id is the primary key column for this table.
--Each row of this table contains information about the salary of an employee.

SELECT
     (SELECT DISTINCT
             Salary
         FROM
             Employee
         ORDER BY Salary DESC
         LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
