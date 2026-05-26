""" 
=> Inverted-Index 
    
    -> Inverted-Index is a core data structure used by search engine like elastic-search 
    
    -> Instead of storing document and scanning them for every query , it maps the each term to the list 
      of documents that contain it 

=> Working 
   
   1. When a document is indexed in elastic-Search , it goes through first an analysis pipeline where text is 
      
      tokenize and normalized 
   
   2. Then each token is stored in an inverted index, which maps the term to a list of document IDs where it appears
   
   3. Along with document IDs, Elasticsearch also stores metadata like term frequency and positions.

   4. During search, instead of scanning all documents, Elasticsearch directly looks up 
      the query terms in the inverted index, retrieves matching documents, and ranks them using scoring algorithms.”   
      
   
   Step 1. Input Document 
               
               "Old laptop in Delhi"
   
   Step 2. Analysis (Processing)   
            
            ["old" , "laptop" , "Delhi"]
   
   Step 3. Build Inverted Index 
           
           "old"    -> [doc1]
           "laptop" -> [doc1]
           "Delhi"  -> [doc1]
   
   Step 4. Add more docs 
          
          Doc 2 = "new phone in delhi"
          
          Now index become 
          
          "delhi' ->  [doc1 , doc2]
          "phone" -> [doc2]
   
   Step 5 Search 
         
         "phone" , "delhi"
         
         Elasticsearch:

         finds "phone" → [doc2]
         finds "delhi" → [doc1, doc2]
         combines results

      returns doc2 first (better match)                                              


     Inverted INdex ====  analysis → indexing → lookup → scoring
     
     -> In scoring 
         
         Es use BM25 algorithm 
         
         term frequency(how oftem word appers)
         inverse doc frequency (rarity of word)
"""