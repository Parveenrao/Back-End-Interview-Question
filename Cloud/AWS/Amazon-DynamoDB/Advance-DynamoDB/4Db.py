""" 

=> TTL (TIme to Live)

   -> TTL is a feature in DyanmoDb that automatically deletes expired items from a table
      after a specified timestamp

   -> instead of manually deleting old , records , we define an attribute and DynamoDB
      remvoes the item after that time

   -> Example 

       1. Session tokens 
       2. Cache entries 
       3. OTP records 
       4. Temporary shopping carts 
       5. Logs 
       6. IoT telemetry 
       7. Notification data 

=> Why do we TTl

   -> Suppose we are storing OTPs

      OTP  =  xxx 

      valid for 5 minutes

   -> Without TTL

     OTP -> Stored forever -> db size increasing forever 

     we would need a cleanup jobs

     cron job -> every hour -> Find expired -> Delete item

     this adds operational overhead

    -> with TTL

        store an expiration timestamp

        expiresat = 175180000

        DynamoDB automatically deletes it after expiration 



        Insert Item

              │

          ExpiresAt

              │

      Current Time > ExpiresAt ?

              │

        YES

              │

       Background TTL Process

              │

         Delete Item


=> background TTL service

                 TTL Scanner

                    │

            Scan Partition Metadata

                    │

                    ▼

           Read Expiration Attribute

                    │

                    ▼

       Current Time >

         Expiration ?

                    │

          YES───────┴──────NO

            │

            ▼

        Queue Delete

            │

            ▼

     Normal Delete Operation

            │

            ▼

        Replicate

            │

            ▼

       Streams Event


=> Does TTL Delete Immediately

   -> No , AWs documents that expired items are typically removed within few days, though

      many are deleted much sooner

=> Does TTl consume Capacity

   1. Userwrite 

       Putitem -> Consume WCUs

   2. TTL delete

      -> background delete 

         consumes , No user WCUs

      TTL deletion do not consume your provisioned write capacity


=> TTl streams 

   -> If dynamoDB streams are enabled

      Item expired -> ttl delete -> Streams -> lambda trigger -> archive or audit or notifications 

      we can react to automatic deletions.

=> Best Practice

    1. Use Unix epoch time(seconds)

        17510000

    2. Do not rely on immediate deletion

        TTL is eventually processed , not instantaneous

    3. Filter expired items in your application

       if item["ExpiredAT"] < current_time:

            # ignore expired item
             
    4. Use stream if you need post-delete processing

       TTL -> Lambda -> Archive -> Analytics

=> Flow 



Client
   │
   ▼
PutItem
   │
   ▼
Leader Replica
   │
   ▼
Write Ahead Log (WAL)
   │
   ▼
MemTable
   │
   ▼
SSTable
   │
   ▼
Item Stored (includes ExpiresAt)
   │
   ▼
──────────────────────────────────
Background TTL Service
   │
   ▼
Scans Partitions
   │
   ▼
ExpiresAt <= Current Time?
   │
 ┌─┴───────────────┐
 │                 │
No                Yes
 │                 │
Keep Item      Internal Delete
                   │
                   ▼
               Write WAL
                   │
                   ▼
              Update MemTable
                   │
                   ▼
                Replicate
                   │
                   ▼
           DynamoDB Streams
                   │
                   ▼
              Item Removed


"""