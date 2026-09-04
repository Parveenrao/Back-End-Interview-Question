""" 

=> DynamoDb Streams

   -> Is a feature that capture every change made to the item in DynamoDb table

      in the order  those changes occur 

   -> Whenever item is

       1. Created (Putitem)
       2. updated (Update item)
       3. Deleted (deleteitem)

    DB automatically writes an event to the stream

=> Why do we need streams

    -> Suppose we have an e-commerce application

        cusomters -> orders table

        Customer place an order

     after the order is saved , we need to

       1. Send an email 
       2. Reduce inventory 
       3. update analytics 
       4. Notify warehouse 
       5. Send SMS

=> Without streams 

    Application 

    Save order -> email , sms , inventory , analytics , warehouse

    application tightly coupled


=> with streams 

   1. Application 

   2. Save order 

   3. Orders table 

   4. DynamoDB Stream

   5. Lambda 

       |-> email 
       |-> sms
       |-> inventory 
       |-> analytics 
       |-> warehouse


    6. application only writes to dynamodb 

    7. Everything else react to the stream


=> Stream Record contains 

                  {
             "eventName": "INSERT",
                  "Keys": {
                   "UserId": "101"
                  },
                "NewImage": {
                "UserId": "101",
                "Name": "Parveen",
                "Age": 24
              }
           }


=> Stream View Types 

   1. KEYS_ONLY

      -> only the primary key is stored

      -> smallest record size and lowest processing overhead 

      -> use when you only need to know which item changed


    2. NEW_IMAGE

        -> Store the image after change

   3. OLD_IMAGE

        -> Store the item before the change

        -> usefull for auditing or rollback scenarios

   4. NEW_AND_OLD_IMAGES

        -> Store both version

=> Stream Shards

    -> Just like table has partitions , the stream has shards

    -> Stream

        |->  shard1
        |->  shard2
        |->  shard3


=> Stream Retention

   -> DynamoDB Streams retain records for 24 hours

   -> if your consumer , does not process them within that window ,they are no longer available

=> Can multiple consumer read the same stream

   -> Multiple application or services can independently consume the stream

=> Is DynamoDB Streams the same as a message queue?

      -> No. A stream is a change data capture (CDC) mechanism tied to table 
        mutations. It's designed to record database changes, not to replace a 
        general-purpose messaging service like a queue.   



"""