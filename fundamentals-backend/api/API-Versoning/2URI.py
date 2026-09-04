""" 


=> URI Versioning 

    -> URI versioning is the most common API versioning strategy where the version number is 
       included directly in the URL

       instead of GET/users

       GET/api/v1/users


    -> Example 

       1.Suppose we are building an e-commerce API

       2. Version 1 

           GET/api/v1/products/101

       3. Later frontend team wants 

          1. Category 
          2. Discount 
          3. Currency
          4. seller details


          if modify the existing response directly , old mobile apps may break

          instead create new version

          GET/api/v2/produts/101         



"""