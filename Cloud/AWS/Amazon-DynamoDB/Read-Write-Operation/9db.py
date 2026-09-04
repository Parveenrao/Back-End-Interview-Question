""" 

=> DynamoDB Transaction Internal Architecture

    -> A transaction may update multiple item , possibly across multiple partitions
       and multiple tables

    -> Challenge is 

        how does DynamoDb ensure either all writes succeed or none of them

    -> To solve this , DynamoDB uses an Internal Coordinator and a protocol similar to

        Two-phase commit

=> High Level Architecture 

                   Client
                      │
                      ▼
              AWS SDK / API Gateway
                      │
                      ▼
          DynamoDB Front-End Router
                      │
                      ▼
        Transaction Coordinator (TC)
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
 Partition A      Partition B      Partition C
 (Leader)         (Leader)         (Leader)
     │                │                │
     ▼                ▼                ▼
 Followers        Followers        Followers


    -> Transaction introduce txn coordinator

=> Step 1 Client Send Transaction 

   Client -> TransactionwriteItems

   Request contain

     Update A , Update B , Put History

   The Front End Router Receives it 


=> Step 2 Router Finds Partitions

    -> Using consistent hashing 

       Account A -> Partition 5 

       Account B -> Partition 17

       History - > Partition 42

       THree physical Partition

    -> Now dynamoDB knows which leader participate


=> Step 3 Transaction Coordinator Created

                     TC
                     │
        ┌────────────┼─────────────┐
        ▼            ▼             ▼
    Leader P5     Leader P17    Leader P42


    Coordinator manage the entire transcation


    Its responsibility include:

       1. Tracking participant
       2. sending prepare request 
       3. collecting votes
       4. handling retries and failures

=> Step 4 Prepare Phase (Phase 1)

    -> Co-ordinator ask every participant

        can you commit

        Coordinator -> Prepare -> P5 , P17 , P42

        each leader performs validation but does not commit yet 

        Typical check

          1. Item exist 
          2. Condition expression pass 
          3. Enough write capacity 
          4. No conflicting txn 
          5. Item size valid 
          6. Permission valid

        Each Participant replies.

          P5 -> Ready

          P17 -> Ready

          P42 -> Ready

          If every participant says Ready

          Coordinator -> Proceed


      -> What happens inside in each leader 

                      Receive Prepare

                             ↓

                  Lock Transaction Metadata

                             ↓

                    Validate Conditions

                             ↓

                     Reserve Resources

                             ↓

                    Write Intent Record

                             ↓

                            READY     

                actual data is not committed 

                only an intent in recorded

                why write an intent

                  -> Suppose server crash

                  without an intent record

                    Did this transaction start -> unknow

                 with an intent

                   Transaction 456

                   Prepared 

                   waiting commit

=> Step 5 Commit Phase (Phase 2)

    -> Coordinator send , commit

       coordinator -> commit 

                          P5 , P17 , P42

       each leader

        apply changes -> update wal -> update Memtable -> replicate -> ack

        only now does the data become visible

=> Step 6 Acknowledgment

    P5 -> ack 

    P17 -> ack

    P42 -> ack


    coordinator receieve all acknowledgment

    all ack -> transaction complete -> return success


   -> what if one partition fails 

      P5 Ready

      P17 Ready 

      P42 Ready

      Coordinator decide  -> Abort 

      Everyone recieve Rollback

      No change become visible

   -> Rollback flow

      Coordinator -> Abort -> P5 -> Discard intent -> unlock

      same for all participants

      since nothing was committed , rollback is inexpensive , pariticipant simply discard 
      the prepared state


   -> conflict detection 

      1. Suppose two transaction update 

          Account A 

          Txn 1 -> balance = -100

          Txn -> balance = -200

          both start simultaneously 

          txn 1 -> account A 


          txn 2 -> account A    


          leader detect conflict 

          one txn Ready

          other Transcation conflict 

          failed txn can retry later 


=> Recovery After crash

   1. Suppose coorinator crash after sending prepare request 

   2. Participant have 

        txn = 123

   3. During Recovery

       Read intent     -> coordinator restart -> continue commit or abort 

=> Why are Txn slower

   -> extra work include

      1. Partition discovery
      2. Coordinator management 
      3. Two-phase commit 

      4. Intent records 

      5. Conflict detection 

      6.Multiple ack

      this is why txn have higher latency and consume more capacity than individual writes

=> Complete Internal Flow 



                 Client
                    │
                    ▼
        AWS SDK / DynamoDB API
                    │
                    ▼
        Front-End Request Router
                    │
                    ▼
        Identify Target Partitions
                    │
                    ▼
      Create Transaction Coordinator
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
  Leader P5     Leader P17    Leader P42
      │             │             │
      ▼             ▼             ▼
 Validate      Validate      Validate
 Write Intent  Write Intent  Write Intent
      │             │             │
      └────── READY Responses ────┘
                    │
          All READY?
           │       │
          Yes      No
           │        │
           ▼        ▼
     Send COMMIT   Send ABORT
           │        │
           ▼        ▼
  Apply Changes   Discard Intents
  WAL + MemTable
  Replicate
           │
           ▼
     ACK to Coordinator
           │
           ▼
     Return Success



"""