""" 
=> QueryPlanner
     
     -> Choose the most efficient way to execute a query using available index 


---------------------------------------------------------------------------------------------------------

=> Step by Step 
    
    let take an example 
       
       db.users.find({"age" : 22 , name : "Parveen"})
    
    
    1. Parse And Normalize
        
        MongoDB rewrite the query into an internal form (order / shape  normalized ) 
    
    2. Generate Candidate plans 
        
        Based on index , it build plans
        
        Use Index (age : 1)
        Use Index (name : 1)
        
        Use compound (age : 1 , name : 1)
        
        Do a full scan (COLLSCAN)
    
    3. Trail Phase (Plan Ranking)
    
       
        -> MongoDB runs a small portion of each plan  and measure 
           
           1. DOCS examined
           2. KEy examined 
           
           3. WORK DONE  (internal metrics)            
           
           Plan with less work will win
    
    4. Select winning Plan
        
        -> That plan is used to finish  the query
    
    5. Plan cache 
        
        -> The winning plan is cached for this query shape           



"""