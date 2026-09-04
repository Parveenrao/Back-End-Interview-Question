""" 

=> Transactions 

    -> Txns In DyanmoDB allow you to perform multiple read and write operations as a
       single atomic unit

=> What is Transaction 

   -> A txn is a group of operation , that either

      1. All succeed , 
      2. All fail 

     There is no partial success

=> ACID Properties 

   -> DyanmoDB txn provide ACID gurantees

   1. Atomicity

       -> All operation succeed together

   2. Consistency 

      -> The db moves from one valid state to another

         no money is created or lost

   3. Isolation 

      -> While a txn is executing , other client don't see partial updates

   4. Durability 

       -> Once committed 

       -> Committed changes are durable


=> Transaction APIs

    1. TransactionWriteItems
     
        -> Support upto action in one txn (subject to dynamo aggregate size limit)

        -> Possible action 

           1. Put
           2. update 
           3. Delete 
           4. Condition check

        -> Example 

           Update account A 

              + 


           Update account B 

               +

             Insert txn history 

          One txn

          
    2. TransactionGetitems

        -> Read multiple items automatically

        -> either all read are consistently or the operation fail      



"""