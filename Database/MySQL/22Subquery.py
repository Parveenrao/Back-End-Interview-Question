""" 

=> Subquery 

    -> A subquery is a SQL query written inside another SQL query

    -> inner query produce a result , and outer query uses that result 


=> Correlated Subquery

   -> A correlated subquery that depends on a value from the current row of the outer query


   Employees whose salary is greater than the average salary of their own department.

    SELECT e1.name, e1.salary
    FROM employees e1
    WHERE e1.salary > (
               SELECT AVG(e2.salary)
               FROM employees e2
               WHERE e2.department_id = e1.department_id
              );

    important part is 

    WHERE e2.department_id = e1.department_id

    e2 belongs to the inner query, but e1 belongs to the outer query.          


"""