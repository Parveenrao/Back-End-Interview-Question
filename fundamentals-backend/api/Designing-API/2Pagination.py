""" 

=> Pagination In APIs

    -> Pagination is the process of breaking large dataset into smaller chunks(pages) instead of
       returning everything in a single response


    -> Instead of returing 10 million users

    -> Return only a subset 

       GET/user?page = 1 &limit= 10


=> Why do we need pagination

    -> Imagine database contains 

        USERS

        --------

        10 Millions Rows


    -> without pagination 

       Database -> 10 Million rows -> Backend -> Serialize JSON -> Network -> Client


    -> Problem 

       1. Huge memory

           -> db send 10 millions records

           backend load into memory

       2. Network bandwidth 

          -> increase so much

       3. Browser crash 

          -> frontend receieve , 5GB JSON

              Browser  freezes

       4. Database Scan
 
            -> DB perform huge scans         

            
                               




"""