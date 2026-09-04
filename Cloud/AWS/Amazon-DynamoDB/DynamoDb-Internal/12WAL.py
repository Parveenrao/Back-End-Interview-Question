""" 

=> WAL In DyanmoDB

    -> Write Ahead Logging

    -> WAL is a sequential log file where every write request is first recorded before it is 
       applied to actual database storage.

    -> log first -> Acknowledge -> Apply to storage later


=> Same idea in DyanmoDB

     Incoming Write -> Write Ahead log (append log) -> ACK to client -> background process updates SSTable


     1. Step 1 

       -> Client send 

     2.  DynamoDB appends to wal 

          -> It does not search anywhere

          -> it simply appends 

          -> Appending is extremely fast 

     3. After WAL is safety stored 

         DynamoDB replies

           HTTP 200 Ok


           CLient think , my write is succeeded

     4. background threads update 

         Memtable (memory)

         SStabe(disk)

        This is asynchronous              


"""