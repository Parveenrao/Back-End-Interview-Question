""" 

=> Duplicate Request 


   -> A duplicate request is the same operation sent to the server more than once , intentionally or
      unintentionally 



   -> why do duplicate request happen

      1. Network Timeout

         client -> POST/payment -> Server Payment completed Response Lost -> Client retries

         The payment was successfull , but the client did not know


      2. User double clicks

         -> Suppose a button is not disabled after clicking


         User -> click -> click again 

         Browser send POST/order 
                      Post/order


     3. Mobile Network

        -> Imagine using UPI on a slow connection

        Phone -> Request  -> Poor Network -> Retry Automatically 


      4. Load Balancer Retry 

         -> Sometime a load balancer retries a request if it think backend fails

         User -> Load balancer -> Server A

         Server A becomes slow

         Load balancer sends the request again

         Now server send the request to server 


         Now two server process the request 


      5. API Gateway Retry 

           Client  -> API Gateway -> Microservice 

           if the gateway does not receive a response quickly 

           retry -> duplicate request 

      6. Queue Redelivery

         -> Message queue usually gurantees at least once delivery


           Producer -> Kafka -> consumer 

           kafka send message again 



=> How we detect duplicate request 

   1. Idempotency Key(Best)

   2. Method Uique constraint

       suppose every order has unique iD

       Retry -> Insert same UUID

       Database reject it


    3. Request Hash

        -> hash the request body

   4. Business ID 

      Txn ID , TXXDDJD

      Store -> TCJHJS

      Ignore or return the previous result        

"""