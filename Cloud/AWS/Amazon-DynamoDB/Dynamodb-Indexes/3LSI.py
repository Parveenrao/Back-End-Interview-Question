""" 

=> What happens Inside DyanmoDB when we write data 


    1. Create table 

        Post 

        Partition key       : UserId 

        Sort key            : PostId


    2. Create and LSI 

        LSI 

        Partition key        : UserId 

        Sort key             : Likes


        Notice that both use the same partition key (UserId) 


    3. Insert first item 

              {
           "UserId": "U1",
           "PostId": "P101",
           "Likes": 20,
           "Text": "Hello"
          }        
    
        Base Table 

          Partition U1 
                P101
       
         
          LSI    

             Partition U1

             20 -> P101

        DynamoDB automatically updates the LSI , we don't need to do anything

    4. Insert another item 


                  {
            "UserId": "U1",
            "PostId": "P102",
            "Likes": 150
           }  

        Base Table 

          Partition U1

             P101
             P102

        LSI

        Partition U1

          20  → P101
          150 → P102          

    5. Insert another item 

                {
        "UserId": "U1",
        "PostId": "P103",
        "Likes": 50
       }           

       Base Table U1

           U1

           P101
           P102
           P103


       LSI 

       U1

      20  → P101
      50  → P103
      150 → P102    


      Base table  is ordered by postid , lsi is ordered by likes

=> What happen during write 

    -> dynamoDB does on write operation from your application point of view , but internally 

       it performs multiple updates

    -> Writing to base table 1 , Update the LSI


=> Why  is it called Local secondary Index 

    -> Because index is local to the same parition key as the base table

    -> it never leave the partition where original item is stored 


=> Where DyanmoDB store it 

    -> It store the index inside the same physical partition

               Physical Partition A

                  Base Table

                    U1
                    P101
                    P102

                 ------------------

                      LSI

                       U1

                  20  -> P101
                  100 -> P102


                  Index never moves to another partition

                  It stays local to the data 


    -> Everything stays inside the same partition

    -> Thats why AWS call it Local secondary index 


=> A Local Secondary Index is called "local" because it uses the same partition key as 
   the base table, so the indexed data remains within the same logical and physical 
   partition as the original item. Only the sort key changes.            


=> Total size of all items sharing the same partition key, including all LSI data 

   cannot exceed 10GB


=> Can we add LSI after creating a table

     -> An LSI must be created when the DynamoDB table is created.

     -> We cannot add , remove , or modify an LSI after the table exist 


=> When to choose LSI 

   1. We want multiple ways to sort items within the same partition key.


=> How are writes to the base table and LSI kept Consistent 

    1. Writes to the base table and LSI are performed atomically as part of the same write 

       operation.

       DynamoDB does not consider the write successfull unitl both base table and LSI
       have been updated 

=> Writes to the base table and an LSI are kept consistent because DynamoDB updates 
   both atomically within the same write operation. Since an LSI shares the same 
   partition as the base table, DynamoDB can modify the base item and its index 
   entry together before acknowledging the write. As a result, an LSI is always 
   consistent with the base table and supports strongly consistent reads. 
   In contrast, GSIs are updated asynchronously, so they are only eventually consistent.       
"""