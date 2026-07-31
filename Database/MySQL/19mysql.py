""" 

=> Types of indexes In Mysql 

    -> Index is a type of data structure MySQL maintain to find rows faster without scanning the
       entire table 


    1. Primary key index 

        -> Created automatically when youd we define a primary key

        -> Unique 
        -> cannot be null
        -> one primary per table

        -> In innodb , primary is the clustered index 

   2. Unique index 

       -> Prevents duplicated indexed values

       -> can contain null values

       -> when we define a UNIQUE constraint, MySQL creates a unique index to enforce it.

   3. Normal / Secondary index 

        Create index idx_name on employees(name)

        -> duplicates are allowed

        -> In InnoDb , secondary index entries also contain the row's primary keys , which 
           mysql can use to locate the complete row

   4. Composite  Index 

       -> One index containing multiple columns

       Create index idx_dept_salary 
        on employees(department_id ,salary)

        Column order matters because of the leftmost-prefix rule.

   5. FullText Index

      -> Used for searching words/text inside large text colums

        Create Fulltext Index idx_description
        on articles(description)

   6. SPATIAL Index

     -> Used for geographic/spatial data.

   7. Prefix Index

       -> Used for long string columns , we can index only the beginning of the values

        Create index idx_name
        on employees(name(20)) 

   8. Covering Index 

       -> Covering index is a type of index that contains all the columns needed to answer 
          a query , so mysql can return the result using only the index without reading 
           the full table row 


           Create index idx_dept_name_salary on 
           employees(department_id , name ,salary)

           select name ,salary from employees
           where department_id = 10;                                   



"""