""" 

=> Cache-Control

    -> Cache control is the most important HTTP caching header. It tells browsers , CDNs and
       other caches whether they should  cache a response , how long to cache it and under what 
       conditions they can reuse it 


    -> why do we need cache control 

       1. Imagine frontend request 

           GET/api/products

      2. without caching 

         browser -> GET/product -> server -> product json

      3. if the user referesh the page 20 minutes 

         20 request 
         20 db queries 
         20 responses 

         This waste bandwidth and increaser server load 


=> Important Tags 

    1. max-age = 60 (keep cache for 60 seconds )

    2. no-cache 

        -> means, you may store the cache , but you must ask the server before using it again 

        cach-control = no-cache


    3. flow 

      browser store response 

      next request  -> can i use this -> server , 304 not modified

      usually used with Etag and last-modified


   4. no-store 

      -> never store this resposne anywhere 

      -> used for sensitive data 

          cache-control = no-store


      -> Browser 

         Do not store in memory 

         Do not save in disk 

         do no cache 


   5. Public

       -> means , anyone may cache this 


         cach-control : public max-age = 3600

       -> good for 

          CSS
          JS
          Images
          Fonts 

   6. Private 

      -> only the user browser may cache it

      cache-control : private , max-age =300

   7. Must revalidate

      -> suppose cache expire 

      -> without this 

         some cache may still serve stale content if the server is temp unavailable

      -> with

          cache-control : must-revalidate

          they must contact the origin server before serving an expired resources 


      -> Example 

         cache-control , max-age = 60 , must-revalidate

         after 60 second 

         browser -> must contact server -> cannot use old response

    8. Immutable

        -> Useful for versioned static assests


        -> header 

           cache-control : max-age = 3124434 , immutable 

        -> browser knows 

           this file will never change 

           do not even revalidate 


from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/products")
def get_products(response: Response):
    response.headers["Cache-Control"] = "public, max-age=300"

    return {
        "products": [
            "Laptop",
            "Phone"
        ]
    }                                                           



"""