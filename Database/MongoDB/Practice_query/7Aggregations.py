""" 
=> Aggregation
    
    -> process data through stage (pipeline) to trasform it
    
    Input -> Stage 1 ->  Stage 2 -> Stage 3 -> Output
    
    -> Basic Syntax 
                    
                    db.orders.aggregate([
                     { stage1 },
                     { stage2 },
                     { stage3 }
                    ])
   
   -> 1. $match (find like filter) 
          
          db.orders.collection([
              
              {$match : {status : "completed"}}
          ])   
   
   -> Project (Shape your data)
       
       db.users.aggregate([
           
           {$project : {name : 1 , email : 1 , _id :0}}
       ])   
   
   -> Group (used for aggregation , sum ,avg ,count)
       
        db.orders.aggregate([
            
            {$group : {_id : "$user_id" , totalSpent : {$sum : "$amount"}}}
        ])
   
   -> sort
       
       {$sort : {totalSpent : -1}}
    
   -> Limit 
   
   -> skip
   
   
---------------------------------------------------------------------------------------------------------

=> Top 3 users who spend most money 
     
     db.collections.aggregate([
         
         {$match : {status : "completed"}},
         
         {
             $group : {
                 _id : "$userId",
                 totalSpent : {sum : "$amount"}},
             
           {$sort : {totalSpent : -1}},
           
           {$limit : 3}  
        ])         
                             

"""