""" 
=> Data-Types 
    
    1. String  
    
        {"name" : "parveen"}
        
        used for text , username , emails
   
   2. Number Type 
       
       1. Integer (32 bit , 64 bit)
       
          {"age" : 22}
       
       2. Double Floating Point 
           
           {"price" : 99.99}
       
       3. Decimal128 for precision 
            
            {"amount" : NumberDecimal("99.99")}       
   
   3. Object ID
       
       -> MongoDb default primary key 
       
       -> Globally unique
       
       -> Contains timestamp  , can be sort by creation time
   
   4. Date 
       
       {"created_at" : ISODate}          
   
   5. Boolean 
        
        {"is_active" : true}
   
   6. Arrays
   
         {
            "skills": ["Python", "MongoDB"]
        }
   
   7. Embedded documents 
       
       documents inside documents 
   
   8. Null 
       
       {"middleman" :null}                          


"""