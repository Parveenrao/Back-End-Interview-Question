""" 

=> Execution of mysql Query 


     SELECT department_id, AVG(salary) AS avg_salary
     FROM employees
     WHERE salary > 30000
     GROUP BY department_id
     HAVING AVG(salary) > 50000
     ORDER BY avg_salary DESC
     LIMIT 5;


     we write it as              => This is mysql Logical order 

     Select
     From 
     where 
     group by
     having 
     order by
     limit


=> SQl Runs it as 

    From -> where -> group by -> gaving -> select -> distinct -> order by -> limit/offset 

    1. From 

       -> Get the source rows first 

    2. where 

       -> filter individual rows , remove the rows which not satisfy the condition before grouping

    3. Group by 

       -> Group the remaining rows 

    4. Having 

        -> Filter the group 

    5. Select 

       -> Produce the requested columns/expression

    6. Distinct 

      -> if specified , remove the duplicate rows 

   7. order by 

       -> Sort the result 

   8. Limit 

      -> Return only the request rows 




"""