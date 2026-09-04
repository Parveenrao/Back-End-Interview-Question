""" 

=> What is Sparse Index

   -> A sparse in DynamoDB is an index that contains only the item that have the indexed 

      attribute 

   -> Unlike traditional database , where every row , is indexed a DynamoDB sparse index 
      automatically exludes items that do not contain the index key attribute 


=> Why it is sparse 

    -> DynamoDB only writes an item into a GIS if the item contains the GSI partition key(sort key,
       if the index define one)


    ->  First understand the problem

         Suppose you have a table called Orders.

             OrderId	CustomerId	         Status	            Total
                O1	      C1	            Pending	              100
                O2	      C2	            Delivered	          250
                O3	      C3	            Pending	              180
                O4	      C4	            Delivered	          90

        Imagine you want to quickly find Pending Orders.

        One way is to scan the entire table. 

        this is expensive for miilions of items 

     -> Solution 

        Create a GSI

        Instead of indexed every order, only index pending order 

        Partition key = pendingflag

        this is called sparse index 


=> Why sparse

    -> Because the index store only a subset of the table

=> Sparse Index a special type of index in DynamoDB?

     -> No. A sparse index is not a separate index type. It is a behavior—typically of a 
       Global Secondary Index (GSI)—where only items containing the index key attributes 
        are included.    


"""