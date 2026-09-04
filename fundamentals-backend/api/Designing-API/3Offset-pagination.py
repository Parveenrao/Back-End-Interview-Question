""" 

=> OFfset Pagination 

   -> Retrieves records by skipping a certain number of rows and then return the next set of rows

      select * from users limit 20 offset 20

      skip first 20 rows and return next 10 rows



   -> Internal Database Execution

       -> many think the database jumps directly to row 100000

       -> it usually don't

       -> suppose limit 5 , offset 10 

          Read row 1 - >discard , read row 2 -> discard -> .....

    -> Large offset problem 

       -> offset 200000
          limit 20

          db scan 20000 rows 

    -> Problem with offset 

       1. slow for large offsets

          offset 5 millions

          db scan/skips 

          return 20 rows


       2. Duplicate records               







"""