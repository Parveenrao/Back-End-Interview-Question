""" 


=> Idempotency In APIs

    -> An operation is idemptotent if performing it multiple time produces the same result as 
       performing it once

        
       1 request = 100 same request 

       Server state should remain the same


=> Why do duplicate Request happen

   1. User click twice 
       -> Buy
       -> Buy
       -> Buy

   2. Internet timeout

      -> Client never receive response

      -> it retires 

   3. Mobile network reconnect

      -> Phone automatically retires

   4. Reverse Proxy Retries 

   5. Payment gateway retires


=> HTTP method are idempotent

   1. GET -> idempotent , does not modify data

   2. PUT -> yes , Replcae resource

   3. Delete -> yes , delete again has not extra effect 

   4. Head -> yes , read only 

   5. Options -> yes , Read only 

   6. POST -> usually No  , create new resources 

   7. Patch -> Usually no , partial updates can accumlate



   
=> Idemptency key

   -> Client generate a unique key 


   -> DB table 

      Key   | status  | response   | created_at



    @app.post("payments")
    def create_payment(amount : int , idempotency : key : str = Header(...)):

       # check is key already exist 

       existing = db.query(Imdepotency).filter(Idemoptency.key = idempotency_key).first()

       if existing:
          return existing.response

       payment = Payment(amount = amount)

       db.add(payment)
       db.commit 

       
    response = {
        "payment_id": payment.id,
        "amount": amount
    }

    db.add(
        Idempotency(
            key=idempotency_key,
            response=response
        )
    )

    db.commit()

    return response

=> Problem Race Condition

    -> Imagine two identical request arrive at almost the same time with the same idempotency key

       Request A 
       Request B

       Both check db -> key exist 

       Both get No because neither has inserted the key yet 

       now both create payment

       payment #1
       payment #2

       this defeat idempotency

    -> solution 

       1. Put a unique constraint on idempotency_key column



=> Should idempotency keys expire

    1. keeping every key forever wastage storage

    2. Store them for 24 hours




"""