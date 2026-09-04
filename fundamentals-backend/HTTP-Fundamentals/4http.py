"""" 

=> Query Parameters 

   -> A query - parameters is key-value pair added to the end of a URL to provide additional 
      information to the server 


      GET/products?=category = laptop

      return only products whose category is laptop


      https://api.shop.com/products?category=laptop&page=2&limit=10
                          │
                          └──────── Query Parameters


=> why do we need query parameters 

    1. suppose db contain 10 millions products

    2. without query paramter

        -> server returns all 10 million products


=> Common Use case 


    1. Filtering

       -> Return product in one category

          Get/products?category=electronics

          GET/products?category=electronics&brand=apple

    2. Searching 

         GET/products?search=laptop

    3. Sorting

        GET/products?sort=price

        descending 

        GET/products?sort=-price

    4. Pagination


    5. Multiple filters 

            GET /products?category=mobile&brand=samsung&price_lt=50000                 





"""