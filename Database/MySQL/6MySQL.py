""" 

1. Delete
    
    -> Remove specific from table with where clause
    -> Can be rolled back inside transaction
    -> slow on larger table
    
    -> Find row
    -> mark it deleted 
    -> Write to undo log
    -> update indexes
    
    -> Lot of work per row , thats why it is fast


2. Truncate
  
  -> Delete all rows 
  -> cannot be rolled back
  -> empty a table completely
  
  
  -> Now row scanning 
  -> no undo log
  -> no rollback
  -> auto increment reset 
  
3. DROP 
   
   -> Delete table + data strucutre
   -> Gone permanently
   -> delete indexes
   
   -> very fast
  
      



"""