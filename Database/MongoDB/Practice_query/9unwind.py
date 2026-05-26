"""

=> Unwind
   
   -> Unwind is an aggregration stage that used to deconstruct an array field from documents and output a separate 
      document for each element in array
   
   
   -> If an document has array 
        
        1. Break that array into multiple documents
        2. Each documents will contain  one element from the array
   
   
   -> Input document 
                
                {"_id": 1,"name": "John","hobbies": ["reading", "gaming", "traveling"]}    
                
                db.collection.unwind({
                    $unwind : $hobbies}
                })   
   
   -> Advance form 
              
              {
                $unwind: {
                 path: "$arrayField",
                 includeArrayIndex: "indexField",   // optional
                 preserveNullAndEmptyArrays: true   // optional
              }
            }    
       
       1. includeArrayIndex => ADd index of each element
                    
                    { "hobbies": "reading", "index": 0 }
                    { "hobbies": "gaming", "index": 1 }    
       
       
       2. preserveNullAndEmptyArrays 
            
            -> Control behaviour when array is 
                
                1. null 
                2. missing 
                3. empty
                
                {
                 $unwind: {
                  path: "$hobbies",
                   preserveNullAndEmptyArrays: true
               }
             }
             
             keep document even if array is empty/null
                                      



"""