SELECT employee_id, CASE
                        WHEN MOD(employee_id, 2) = 0 OR name like 'M%' THEN 0
                        ELSE salary
                    END as bonus
                    FROM Employees
                    ORDER BY employee_id
