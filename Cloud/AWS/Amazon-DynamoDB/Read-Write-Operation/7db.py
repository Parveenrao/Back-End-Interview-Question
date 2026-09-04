""" 

=> Idempotency

    -> An opertion is idemptotent if performing it multiple time has the same effect as performing 
       it once

       1 request -> same result 
       2 request -> same result 
       3 request -> same result

=> Why idempotent important

   Imagine a client sends a request to DynamoDB

   Client -> Putuser(User1) -> Networktimeout

   The client does not whether 

   1. DynamoDB successfully stored the item or 
   2. the request never reached Dynamodb

     
       so client retries

       Retry -> PutUser(User1)

       without idempotency , the same operation might execute twice , causing incorrect data

=> How to make  operation Idempotent

   1. Use the same primary key


       orderId = 1001 

       Retry 

       orderId = 1001

       The same item is overwritten instead of creating duplicates

   2. Use conditional writes

      PutItem

      Condition:

      attribute_not_exist(OrderId)

   3. Use Client Request IDs (Idempotency keys)

      -> Many distributed system generate a unique request ID

         Request ID

         ABC-12345

         Server stores

         ABC-12345

         processed


         -> if client retries with the same ID

            Already processed -> Return previous result -> Do no execute again       



"""