""" 

=> Global Secondary Index

      -> A GSI is another DyanoDB table managed automatically by DyanmoDB

      -> most think , GSI is just an index like in Mysql

      -> Internally , it behave much more like separate distributed table 

=> Why Global 

   LSI -> Same Partition key 

   GSI -> Can have different partition key

          city 
          dept
          Email 
          Status 
          orderDate

    it is global because it is partitioning independent


=> Internal Architecture 

   -> Think of DynamoDB maintaining two distributed tables 


                Write

                  |
                  V

           +----------------+
           | Base Table     |
           +----------------+
                  |
                  |
           Replication Stream
                  |
                  V

           +------------------+
           |   GSI Storage    |
           +------------------+

           
           GSI recieve changes asynchronously 

=> GSI has its own storage files

    wal -> memtable -> Sstable

    exactly like another dhyanmodb table

=> GSI is asynchronous 

   base table -> write completed -> Stream generated -> background worker -> Update GSI

=> Stream

   -> Every successfull write generate 

      INSERT 

      MODIFY 

      REMOVE 

      This enter an internal stream


    base Table ->  Internal Queue -> GSI worker

    worker continuously consume changes 


=> GSI offer eventual consistency

=> Delete flow 


    base table  -> Delete succeeds -> Streams -> GSI worker -> delete from GSI
"""