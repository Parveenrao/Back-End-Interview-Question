""" 
=> Bulk Operation 

   ->  A bulk operation means performing the same operation on multiple resources in a single 
       API request , instead of sending hundreds of request 


   -> Example 

        POST/users 
        POST/users
        POST/users


        We send

        POST/users/bulk


=> WHy Bulk Operation 

    1. Imagine HR system importing 50,000 employees

    2. Without Bulk APIs

       Client 

        POST/employee(john)
        POST/employee(Parveen)
           |
           |
           |
           |

         50,000 request 

    3. Problems 

      1. Huge network overhead
      2. slower 
      3. More tcp connection
      4. more authentication check
      5. server load increase       



"""