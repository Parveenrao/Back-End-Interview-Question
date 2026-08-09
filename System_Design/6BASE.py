""" 

=> BASE (Basically Available , Soft State , Eventually Consistent)


     -> Introduction 

        In distributed system , data is often stored across multiple server or replicas 

                Application
                     |
              Load Balancer
              /     |      \
             /      |       \
          Server1 Server2  Server3
             |      |        |
            DB1    DB2      DB3


        Now imagine a user change their username 

        Parveen -> Parveen Yadav

        Ideally , every replica should immediately contain

           DB1 -> Parveen Yadav 
           DB2 -> Parveen Yadav 
           DB3 -> Parveen Yadav 

        But distributed system have problems such as network delays , server failures ,and 
        network partitions 


        SO temporarily we got 

        DB1 -> Parveen Yadav 

        DB2 -> Parveen Yadav 

        Db3 -> Parveen


        We now have a choice:

            Should the system stop serving request until every replica agrees , or 
            should it conitnue working and allow temporary inconsistency

        -> BASE choose the second appraoch 

            Base is a design philosophy for distributed system that emphasizes availability 
            and eventual convergence rather than requiring every replica to be immediately
            consistent 

        -> SO the core idea is 

           Keep the distributed system available even if the data is temporarily 
           inconsistent and synchronize the data over time so replica eventually agree 



=============================================================================================

=> Basically Available 

   -> Basically available means , system tries to remain available to users even
      is some server fail  , the network is slow or replicas are 
      temporarily inconsistent

   -> In other words , 

      The system prefer serving a response instead of failing the request 

   -> Basically , Does not mean 100% availability.

       It means the system will do its best to serve request under failure 

   -> why do we need it 

      1. Imagine you have e-commerce website 

                 User
                  |
             Load Balancer
          _______|_______
         |       |       |
       Server1  Server2  Server3
         |       |       |
         DB1     DB2     DB3          


         Normal search follows

         A customer every searches for iPhone

         Normally every search works

         User -> Server2 -> Db2

         Resposne comes in millisecond

      2. Now suppose DB2 crash

          Now the system have two choices

          Option 1 -> Strong consistency

             -> Return an error , 503 Unavailable 

                THe customer cannot browse products 

                Availability is lost 

          Option 2 (BASE)

             -> Instead of failing , request is redirected 

                User -> Server 2 -> Db2 -> Retry -> Db1

                The user still recieves product information

                Maybe is a few second old , but the webiste keep working

                This is basically available 


=> Important Interview Point

     -> Basically Available does NOT mean the data is always correct.



      -> The system prefers returning some response rather than no response.


      -> Slightly stale data
      -> Partial data  
      -> Cached data
      -> Data from another replica                                

=================================================================================

=> Soft State 

    -> Soft State means the state of a distributed system can change over time 
       even if no new user request arrives 

       why 

       Becuase the system is continuously synchronizing replicas in the background

       The data is not fixed immediately after write 


   -> Example 

             User
              |
          Write Request
              |
      ---------------------
      |        |         |
     DB1      DB2      DB3    


     Initially ,

     DB1 : Balance = 1000Rs

     DB2 : Balance = 1000Rs

     Db3 : Balance = 1000Rs

     Everything is synchronized 


     User perform an action , User deposite 500

     Balance 1000Rs -> 1500Rs

     Request Reach DB1 first 

     DB1 : 1500

     DB2 : 1000

     DB3 : 1000

     Why , Because Replication takes time

     No New request arrives 

     Nody perform another transaction

     Nobody Reads and Write , Nothing 

     After few Millisecond

     DB1 : 1500
     DB2 : 1500 
     DB3 : 1000

     After few second

     DB1 : 1500
     Db2 : 1500
     Db3 : 1500

     -> Nothing something interesting
        
         System state changed

         without any new client request 

         Because background replication was happenin 

         Thats exactly what soft state means 

   -> Why it is called Soft 

        1. Hard State 

            Once updated , it never chagnes unless another user request arrives 


        2. Soft state 

           -> It can evovle over time

           User writes -> One replica updates -> replication -> Another replica updates 

           -> another replica updates


=> Soft State means the state of a distributed system is allowed 
   to change over time without new client requests because replicas, 
   caches, and other components synchronize asynchronously in the background. 
   This temporary instability is expected until the system converges.   


=======================================================================================


=> Eventually Consistent

   -> Eventual Consistent means , that if no new update are made to a piece of data 
      all replica will eventually converge to the same value

   -> Keyword is eventuall

   -> It does not mean 

      1. Immediately 
      2. Within 1 second 
      3. Wihtin 5 second 
      4. Within 1 minute 


   -> It simply means ,

       Given enough times and no further writes , every replica will become
       consistent

   -> Eventually Consistent means that if no new updates are made, 
       all replicas are guaranteed to converge to the same state after
       background synchronization completes.

       The condition "if no new updates occur" is essential.  

   -> Eventually Consistent means that in a distributed system, 
      if no further updates are made, all replicas will eventually 
      converge to the same state after asynchronous replication 
      and background synchronization complete.            

      
====================================================================================

=> When to choose ACID 

   1. Choose Acid when correctness is more important than availablility or 
      performance 

   2. If inconsistent data can cause financial loss or legal problems , use ACID

      1. Banking 

          -> Atomicity 
          -> Consistency 
          -> Isloation 
          -> Durability

      2. Payment System

          -> Imagine payment succeed but the order is not created

              or the Order is created twice 

              This is unacceptable

              Strong transaction are required 


=> When To Choose BASE 

    -> Choose when availability and scalability are more important the  immediate 
       consistency

       1. Facebook likes 

       2. Instagram followers 

       3. Youtube view count 

       4. Product Reviews





"""