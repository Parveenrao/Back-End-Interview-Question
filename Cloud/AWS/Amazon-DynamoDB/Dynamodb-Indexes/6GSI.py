""" 

=> Projection Types 

   -> Which attribute from base table are copied into an index (LSI or GSI)

   -> Instead of copying the entire item into the index , DynamoDB lets you chooose 
      what data should be stored in the index

   -> Reduce storage cost and improve query performance


=> How index store data 

    1. Every index always stores

       -> index partition key 
       -> Index sort key (if present)
       -> base table primary key 

       -> Project attributes



=> Three Types of Projection 

   
   1. KEYS_only Projection 

       -> Only keys are stored , For a GSI

         GSI Partition keys 

         GSI sort keys 

         Base table PK 

         Base table SK


   2. INCLUDE projection 

       -> Store only selected non-key attributes


   3. All projection 

       -> Everything is copied             



"""