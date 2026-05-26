""" 
=> Bloom filters 
     
     -> Bloom filter is a probabilistic data structure used to anser 
          
          "Have i seen this element before"
         
         
        if says no     --> definitely not present 
        if it says yes --> maby be present (could be false positive)


---------------------------------------------------------------------------------------------------

=> In real system 
    
    checking database everytime is so expensive
    
    ex -> username check , cache lookup before db hit 
    
    so we use bloom filter as pre-cache layer
    

---------------------------------------------------------------------------------------------------

=> Working of Bloom filters 
    
    -> Bloom filters has two things 
        
        1. Bit array of m size 
            [0, 0, 0, 0, 0, 0, 0]
        
        2. K hash functions 
            
            h1 , h2, h3, h4
  
  
  -> Insert operation 
  
       ex = dog 
       
       h1(dog) = 2
       h2(dog) = 5
       h3(dog) = 7
       
       set bits to 1 
   
   [0, 0, 1, 0, 0, 1, 0, 1]
   
   ex = cat 
   
   h1(cat) = 1
   h2(cat) = 5
   h3(cat) = 6
   
   position 5 was already filled
   
   
2. Search operation 
    
    ex = lion 
    
    h1(lion) -> 1
    h2(lion) -> 5
    h3(lion) -> 7  
    
    all bits are one , bloom filter says "Present"
    
    but lion not inserted  , False Positive


--------------------------------------------------------------------------------------------------------

          ┌──────────────┐
          │  User Input  │
          └──────┬───────┘
                 ↓
        ┌─────────────────┐
        │ Bloom Filter    │
        └──────┬──────────┘
               ↓
     ┌─────────┴─────────┐
     ↓                   ↓
 NOT present        MAYBE present
     ↓                   ↓
Accept instantly     Check Database
                         ↓
                Exists? → Reject
                Not exists → Accept     
                                    

1. Update Bloom filters after DB insert 
      
      when new username is created 
         
         insert into DB  -> then update bloom filter
         
         keep filter refersh

2. Use cache 
    
    bloom filter -> cache -> Db


        Request
          ↓
      Bloom Filter
          ↓
      Cache (Redis)
          ↓
       Database              


-> As data grows n increase , more false positive rate increase 


"""