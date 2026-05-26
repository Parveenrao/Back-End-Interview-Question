"""" 
=> Document
   
   -> A single record stored as a key - value pair (like json)
                  
                  {
        "name": "Parveen",
        "age": 22,
        "skills": ["Python", "MongoDB"]
          }
          
          Entire thing , one document

   
   -> Properties 
      
      1. Key-value Structure 
         
         Each field has
         
         key(string)
         
         value(anytype)
         
         {
             "name" : "Parveen",  // string 
             "age" : 22 ,         // number 
             "isActive" : true    // boolean
         }
      
      2. Unique Identfier (_id)
         
         Each document has unique id
         
         {
         "_id": "auto-generated",
         "name": "Parveen"
         }   
         
         -> Primary key of document 
         
         -> Must be unique
         
         -> Auto generated if not provided 
      
      3. Nested Document 
          
          Documents can store another documents 
            
            {"name" : "parveen" ,
            
              "address" : {
                  "city" : "delhi",
                  "pincode" : "123303"
              }
            }   
       
       4. Arrays support 
           
           {
               "skills" : ["python" , "MongoDb"],
               "marks" : [90 , 85 , 88]
           }     
       
       
       5. Max document Size = 16MB    

"""