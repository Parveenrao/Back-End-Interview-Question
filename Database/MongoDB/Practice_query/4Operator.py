"""" 
=> Operator 
     
     -> Operatora are special keyword (starting with $) used to 
          1. filter data
          2. update data
          3. transform data




----------------------------------------------------------------------------------------------

1. Query operator 
      
      They are used inside 
      
      db.collection.find({})
      
      They help you filter document based on conditions
      
      All query operator start with $


2. Comparison operator
      
      syntax  {field : {$operator : value}}
      
    ->  // greater than 
          
          db.users.find({age : {$gt : 25}})
    
    ->  // less than 
        
         db.users.find({age : {$lt : 25}})
    
    -> //range 
         
         db.users.find({age : {
             $gte : 25 , $lte : 30
         }})           
    
    -> // not equal 
        
        db.users.find({
            age : {$ne : 18}
        })     
    
    -> // multiple 
                          
       db.users.find({role: {$in  : ['admin' , 'users']}})
    
    -> // not in 
        
        db.users.find({role : {$nin : ['banned]}})   

3. Logical Operator 
     
     -> and , mongodb use it explicitly
     
     
     -> or , any condition should match 
     
     
     -> nor (None of these match)
     
         db.users.find({
             $nor: [
                 {age : {$lt : 18}} ,
                 {status : "banned"}
             ]
         })    
     
     -> not 
                        
             db.users.find({age: { $not: { $gt: 30 } }})    
 
4. Element operator 
    
    -> $exist  
            
            db.users.find({ phone: { $exists: true } })
    
    -> type 
              
              db.users.find({ age: { $type: "int" } })


5. Evalution Operator 
   
   -> regex operator 
          
          
          db.users.find({name: { $regex: "^Par", $options: "i" }})                                        
         
         Starts with par , case insesitive
   
   -> $expr 
           
           db.products.find({$expr: { $gt: ["$price", "$discountPrice"] }})  

6. Array Query operators
  
  -> $all 
     
     db.user.find({skills : [$all: ["mongodb" , "node"]]}) 
     
     must contain all values
   
   -> size 
       
       db.user.find({skills : [$size : 3]}) 
   
   -> elematch 
               
               db.students.find({scores: { $elemMatch: { $gt: 80, $lt: 100 }}})        
               
     match multiple conditions inside array           
"""