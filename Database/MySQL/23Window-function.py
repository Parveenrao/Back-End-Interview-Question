""" 


=> Window Function 

    -> A window function perform a calculation across a group of related rows while 
       keeping every individual rows in the result 


     Group by -> combines rows 

     Window function -> keep rows and calculate across them


    -> Over()

       -> Calculate avg(salary) over a particular set/windows of rows

    -> Partition by()

       -> Divide rows into logical groups without collapsing them


   ->  PARTITION BY means divide the rows into separate groups for the window function's 
       calculation, but keep all original rows.              

       

=> Ranking Window Function 

    1. Row_Number()

       -> Row number is window function that assigns a unique sequential number to every row 
          based on the order we specify

       -> Even though two employees have same salary but row_number give them unique sequence 



   2. Rank Window Function 

        -> RANK assign a rank/position to each row based on ordering

        -> when two rows have same values , RANK give them same rank and skips the next rank

   3. DENSE RANK 

       -> Assign rank based on ordering 

       -> They get the same rank 

       -> The next rank is not skipped 

       -> when two rows has same value , they get same rank


   4. LAG

      -> LAG is used to access a value from a previous row 

      -> LAG = look backward        

      -> LAG() is a window function used to access a value from 
         a previous row within the window, based on the ordering specified in OVER(). 
         It is commonly used for period-over-period comparisons, growth calculations, 
         and detecting changes between consecutive rows.  


   5. LEAD 

      -> Lead gets a value from a following row based on the ordering of the window 

      -> like we want to see next month sales 

      -> LEAD() is a window function that accesses a value from a 
         following row within the window based on the specified ordering. 
         It is useful for comparing the current row with future/next rows without 
         using a self join.             

"""