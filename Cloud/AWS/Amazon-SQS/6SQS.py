""" 

=> SQS FIFO
  
    -> How does Amazon SQS maintain ordering in a distributed system without sacrificing all scalability.



    -> Problem 

       Suppose a banking application send these transactions

        withdraw = 100 
        deposit = 500

        check balance

       if they are execute in order 

       Balance = -1000

       withdraw = 100 => 900

       deposite = 500 , 1400

       check balance = 1400


    Now imagine multiple  consumers process them out of order

    Deposit 500

    Withdraw = 100 

    check balance

    result should be incorrect depending on busniess logic

    financial system requiring strict ordering


=> Why Standard Queue Cannot gurantee Order

                               Queue
                         ┌──────┼──────┐
                          ▼      ▼      ▼
                   Partition1 Partition2 Partition3

        message are spread across multiple partitions

        A -> Partition 1 
        b -> Partition 2 
        C -> Partition 3

     Consumer Read independently

     Result , A C B

     This is acceptable for image processig and email jobs , not for payments


=> FIFO Architecture

    -> FIFO introduce an additional Concept

      Producer -> message Group ID -> FIFO queue -> order processing

      the message group id is the key to FIFO

    -> Message GroupId

        Suppose we have orders for two customers

        Customer A 

           Order 1 
           Order 2 
           Order 3

        Customer B

           Order 1 

           Order 2 

           Order 3

        Instead of treating them all as one sequence 

        A1 A2 A3 A4 B1 B2 B3

        SQS store them as sequence 

        Group 1 -> A1 A2 A3 

        Group 2 -> B1 B2 B3

        Each group preserve its own order

    -> Consumer scheduling

        Suppose we have two workers

        worker 1 , worker 2

        Internally , Group 1 -> Worker 1 , Group 2 -> worker 2

        both groups are processed simulatenosuly 

        within each group , order is preserved

    -> Internal Group lock

        Group A -> Assigned -> worker 1

        until worker 1 : DeleteMessage()

        No other consumer receive another message from group A

    -> After delete

        worker finish: Delete A1 

        immediately Deliver A2

        Then Delete A2 

        Deliver A3

        Exactly one message at a time per group


=> Internal Scheduler

    -> Imagine thousand of groups

       Group A 

       Group B 

       Group C

       Group D 

       Group E

       Scheduler maintains like

       unlocked groups -> choose next groups -> Assign consumer

       locker groups are skipped


=> Deduplication Problem

    -> Suppose producer crashes

       Producer -> Send message -> network failure

     Producer does not know if sqs received it 

     it retries 

           Send again

           Now there are duplicates

=> Deduplication ID

   -> Follow allows a dedupID

   -> Internal cache:

       Recent Dedup IDs

        Order123

        Order124 

        Order125

    if order 123

       arrives again with the dedup window

       SQS ignore the duplicate 


=> Standard queue -> Work in parallel

=> FIFO -> Group A -> sequential processing

   because ordering must be preserved. SQS cannont process multiple message from same group

   simultaneously 

=> Flow 

  Producer
     │
     ▼
Message Group ID
     │
     ▼
Deduplication Check
     │
     ▼
FIFO Storage
     │
     ▼
Group Scheduler
     │
     ├─────────────┐
     ▼             ▼
Group A        Group B
     │             │
Worker 1       Worker 2
     │             │
Delete          Delete



"""