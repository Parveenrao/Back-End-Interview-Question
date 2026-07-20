""" 


=> Based On Communication 

  
=> 1 Rest APIs

    -> Representational State Transfer

    -> Is an architectural style for designing web APIs

    -> It use HTTP methods like GET , PUT , POST , Patch and DELETE to perfrom operation on
       resources such as orders or products

    -> Everything is treated as resources , orders , prodcuts are resources indentified
       by URLs. Operation are performed using HTTP method


    1. Representation 

       -> Suppose a user exist , inside the database , the db store the real object

       -> when client ask GET/user/5 , db does not send db rows , instead it send representation

                   {
                 "id":5,
                 "name":"John",
                 "age":30
                 } 

    2. State

       Data moves 

        Client -> HTTP -> Server

        or 

        Server -> HTTP -> Client

        transfer happen continuously             

    3. State 

       -> State simply means , current condition

         cart empty -> item added -> payment done 

         each step changes state 

         Rest transfer information that reflects or changes this state


"""