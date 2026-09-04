""" 

=> What is Index Consistency 

    -> After updating the base table , how quickly does the index reflect that change


    1. LSI 

       -> Local secondary index is strongly consistent

       -> Because LSI is stored in the same physical partition as the base table 

       -> Since both are in same physical partition

           1. write base table 
           2. update lsi 
           3. Commit 

        write succeeds only after both are updated


    2. GSI

       -> Is eventually consistent

       -> becuase GSI is stored separately from base table 

         base partition -> Replication -> GSI partition

         client get updated  before GSI updated     



"""