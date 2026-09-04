""" 

=> Vary
 
   -> tells cache which headers affect the response , so they  know when to use a cached response
      and when to store a separate one


   -> client 1

       GEt/greetings

       Accept-Language - en

       server 

       200 ok

       vary : Accept - lang

       hello

    -> client 2 

        GET/greetings

        Accept-lang : fr


    -> without vary , cache might incorrectly serve "hello" to french user 


    -> with vary , 

       cache store , separate cached response for eng and fr 


=> Vary → Tells caches which request headers determine whether a cached response can be reused.                    




"""