""" 
=> Transaction
    
    -> A transaction is a group one or more sql operation that treated as single unit of work
       
       either all operation succedd
       or none of them are applied
       
       
        START TRANSACTION;

        UPDATE accounts SET balance = balance - 100 WHERE id = 1; 
        UPDATE accounts SET balance = balance + 100 WHERE id = 2;

        COMMIT;
     
    -> Transaction Flow
       
       1. start transaction
       2. queries executed in memory / buffer
       3. changes written in redo log
       4. commit
           
           -> data flushed to disk (permanent change)
       5. Rollback
           -> Undo using undo log
    
    
-----------------------------------------------------------------------------------------------------------------------

=> Core transaction commands
    
    1. Start txn / begin 
    2. commit
    3. rollback
    
    4. savepoint
        
        -> create a checkpoint inside a transaction 
        
       savpoint sp1;  
        
    5. Rollback to savepoint 
       
       rollback to sp1;
    
    6. Release savepoint 
        
        Release savepoint sp1;
    
    7. set txn (isolation levels)
    
    8. set autocommit 
       
       set autocommit = 0; disable auto commit 
       set autocommit = 1                     
       
    -> Example 
       
       
       
       START TRANSACTION;

       UPDATE accounts SET balance = balance - 500 WHERE id = 1;

       SAVEPOINT after_deduction;

       UPDATE accounts SET balance = balance + 500 WHERE id = 2;

       -- something went wrong
       ROLLBACK TO after_deduction;

       -- fix issue and try again
       UPDATE accounts SET balance = balance + 500 WHERE id = 2;

       COMMIT; 
    
    
    -> cons 
       
       1. forgot commit
           
           -> txn open for long time = lock held = slow system
       
       2. long txn 
          
          -> lock contention
          -> deadlock 
          -> replication lag             
"""