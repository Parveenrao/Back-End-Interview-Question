"""
=> Index 
     
     -> Index is a logical container of documents  , optimized for search 
     
      -> In Elastic-Search 
          
          Index -> Documents -> Fields 
     
     -> Example   Product Index
                    
                    {
                         "name" : "iphone 13",
                         "price" : 50000,
                         "category" : "mobile"
                    } 
                    
                    -> This document lives inside product index 


------------------------------------------------------------------------------

=> Normal database just store data 

=> Elastic Search Index does 3 things 
    
    1. Store data 
    
    2. Build Search Structure (Inverted Index)
        
        when you insert "iphone 13 pro"
        
        it transform into 
        
        iphone - doc1
        13 - doc1
        pro - doc1
    
    3. Apply Analysis 
        
        -> Before storing it  
         
         lowercase         -> IPHONE = iphone 
         remove stopwords  -> "the" , "is"
         tokenize words      
         
         -> Controlled by analyzer  
                                 

"""
