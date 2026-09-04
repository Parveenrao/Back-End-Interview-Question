""" 


=> Safe Method 

   -> A safe method is one that does not change the state of the server 

   -> server shoudl not create, update or delete any data when handling  a safe request 

   -> Safe methods are used only for reading information


=> Safe HTTP methods 

   1. GET      -> Reads data 
   2. HEAD     -> Reads header only 
   3. OPTIONS  -> Return supported methods 
   4. TRACE    -> Echoes request 


=> WHy PUT is idempotent but no safe 

    1. Suppose name = "John"

    2. PUT/users/1

         John -> Parveen 

    3. Run it once  

        Parveen -> Parveen 

    4. Final state is the same no matter how many times you send it , so its idempotent


    5. But it changed the database , so it is not safe 


=> Why Delete is Idempotent but not safe 

    Name = Parveen

    1. First Request 


        DELETE users/1 

        db -> empty 

    2. Run it again 


       db -> empty 

    3. Result is the same , no matter how many times we run it 

    4. Not safe , because it changed the db state       



"""