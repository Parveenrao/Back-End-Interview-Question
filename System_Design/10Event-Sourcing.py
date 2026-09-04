""" 


=> Event Sourcing Pattern

   
   -> It is used in system where every change matter , such as banking , trading , e-commerce
      healthcare and inventory management.

    -> Instead of storing current state , we store every event that happened



    -> Example , Normal Database approach 

        1. Initially bank balance = 1000

           user deposite = 500  


       2. db become = 1500


       3. Userd withdraw 200

       4. db become = 1300

       5. current table 


          id                   balance    
          101                   1300

          where is the history , it gone unless we maintain audit table

    -> Event sourcing approach

        1. Instead of storing 1300

        2. we store every event 

            1. Account created 
            2. Money   deposited 
            3. Money   withdraw
            4. Money   deposited 
            5. Money   withdraw   



=> Definition 

  Event sourcing is a architectural patten where every change to an application state is stored 

  as an immutable event instead of overwriting the current state

"""


""" 

=> Component 

   1. A commands means i want to do something

        -> createOrder 

        -> CancelOrder

        -> DepositMoney

        -> TransferMoney 

        -> PlaceBid


   2. Command Handler 

       -> handle validate


           is account active 

           enough balance 

           fraud 

           permission

   3. Event 

      -> Event represent something that already happened


      -> example 

          money deposited 

          money withdraw

          usercreated 

          productadded 

          email sent


   4. Event store 

      -> instead of SQL update

         update account 

         set balance = 1300


         1. we append

            Event # 1

            account created

            Event # 2

            Money deposited

            Event # 3

            MoneyWithdraw


            Nothing is modified 

            Only append 

            This is called  appen-only-log


   -> Aggregrate 


       -> Aggregrate is the object whose state is rebuilt


           bankaccount 

           order 

           shopping cart

           invoice

        every aggregrate has a unique id 

        example = account -101

        all events belongs to it


    -> Event replay

        1. imagine production crashed

        2. database lost 

        3. only event log exist 


        
                                                  



"""