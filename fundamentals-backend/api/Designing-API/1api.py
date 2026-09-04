""" 
=> Principle of Designing Good RestAPI


   1. Used Nouns , not verbs

       -> Rest is resource oriented

          GET/users
          POST/users
          DELETE/users/10

   2. Use Plural Resources Name

      -> Resources usually represent collection

          /users
          /products
          /orders
          /books

   3. Use Proper HTTP methods


   4. keep URLs simple

      GET/customers


   5. Use Hierarchical URLs

      -> Suppose every user has post 

        /users/10/post 

   6. Use Query Parameter for filtering


   7. Use pagination

      -> Never return one million records

          GET/users -> bad 

          good -> GET/user?page = 2&limit = 20

   8. Allow sorting


   9. Support searching 

   10. Version API

      api/v1/users

      api/v1/users

   11. Return proper HTTP status codes


   13. Use meaningful error message

   14. Validate Inputs

      -> Instead of accept everything 

      -> validate

         Email 

         Password 

         Date

         Number range 

         Required fields

   15. Do not expose internal database IDs Unnecessarily 

   16. Use HTTPS

   17. Authentication

       Never pass password In URLs

   18. Do not leak sensitive information


   19. Document Your API

      -> Good documentation include 

         1. Endpoint 
         2. HTTP method 
         3. Request body 
         4. Path parameters 
         5. Query parameters
         6. Headers 
         7. Error Response 
         8. Authentication requirements


=> Real Life example 


Example: A Well-Designed REST API

Assume we're building an e-commerce API.

Operation                     	Endpoint
Get all products	              GET /products
Get a product	                  GET /products/{id}
Search products	                  GET /products?search=iphone
Filter by category	              GET /products?category=mobile
Sort by price	                  GET /products?sort=price
Pagination	                      GET /products?page=2&limit=20
Create product	                  POST /products
Replace product	                  PUT /products/{id}
Partially update product	      PATCH /products/{id}
Delete product                    DELETE /products/{id}
Product reviews	                  GET /products/{id}/reviews
Create review	                  POST /products/{id}/reviews



"""