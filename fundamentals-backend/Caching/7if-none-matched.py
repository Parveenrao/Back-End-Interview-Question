""" 

=> If None-matched 

   -> Is an HTTP request header with Etag

   -> it tells server 

       I already have this version of the resources. only send me the data if it has changed


=> why do we need if none-matched

   -> suppose browser already downloaded
    
        GET/products


       server responded 

        HTTP/1.1 200 ok

        Etage : "abc123"


        browser store 

          Products + Etag

    -> Next Request 

       After the cache expire (or if cach-control: no-cache is used) the browser sends 


        GET/products

        if none-matched : "abc123"


        The browser does not create the value abc123

        it simply copies the Etag that the server gave it previously 


=> What does the server do

   -> server generates the current etag for /products

   -> suppose it sill
        abc123

   -> now compare 


      Browser abc123 -> server 123 

      server says copies is still valid

      browser used it cached copy 


=> what if data changed 

    new Etag -> zcvcv4r345

    browser still send 

       if none-matched : "abc123"

       not equal


       browser updates its cache with
        
         1. New json 
         2. New etag 


=> Easy way to remember
ETag = Server says: "This resource is version abc123."
If-None-Match = Client asks: "Is my version abc123 still the latest?"         




"""