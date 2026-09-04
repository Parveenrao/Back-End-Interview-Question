""" 

=> URI , URN , URl

    -> URI = Unifomr Resource Indentifier 

    -> URL = Uniform Resource Locator 

    -> URN = Uniform Resource Name


=> 1. URI (Unform Resource Identifier)

   -> A URI is anything that identifies a resources

   -> IT does not matter whether it tells you where the resource is or not


=> 2. URL (Unifrom Resource Locator)

   -> A URL not only identifies a resources but also tells you where it is located and how to access
      it

      https://api.example.com/users/10
       |      |            |
       |      |            |-> Resource path
       |      |-> Domain
       | 
       -> Protocol

=> URN (Uniform Resource Name) 

   -> A URN identifies a resources by name , not by location

   -> example , urn:isbn:9780134685991 , This identifies a specific book by its ISBN

   -> It does not tell

       1. which server has it
       2. Which website store it 
       3. how to download it


=> In REST APIs

    suppose we have GET Https:// api.shop.com/products/10

    The request uses.

     https://api.shop.com/products/10

     This is both 

       URL
       URI

       


"""