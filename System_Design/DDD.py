"""" 
=> Domain Driven Design
     
     -> Designing software based on real busniess problems (domain) not just database and tables or API
         
         Instead of thinking i need 
            
            controller --> service ---> model
         
         we think 
         
           what problem this busniess solve , and how do i model that in code
           

-------------------------------------------------------------------------------------------------------

=> Step 1.  

    -> What is Domain
         A domain is the business are your software solve 
         
         E-commerce ---> orders , payment , inventory
         Ride app  ----> driver , tips , pricing

=> Step 2
    
    -> Core idea 
       
       1. Put business logic at the centre , everthing else support it
       
       2. Business-first design


=> Step 3 Building Block DDD 
        
        1. Entities 
            
            -> Objects with Entities 
            
            class User:
               def __init___(self , id , email):
                   self.id = id 
                   self.email = email 
                   
                 if email changes , still the same user , id is same
        
        
        2. Value Objects 
            
            Only value matters
              
              class Money:
                 def __init__(self, amount , currency):
                     self.amount = amount
                     self.currency = currency
        
        3. Aggregrate 
             
             -> Clusterd of related objects  with one root
                          
                          Order (root)
                            ├── OrderItem
                            ├── PaymentInfo      
                    
                    always go through orders 
         
        4. Domain Services 
            
            -> Logic that does not belong to single entity
        
        5. Repositories 
             
             -> How you access db
             
             -> Domain does not care about postgress, mysql
        
        6. Bounded Context 
            
            -> Big system -> split into smaller domains
            
            userservice, 
            payment service 
            item service 
            
            has its own 
            
            model , logic , rules
            
            no tight coupling                                                               

                
              

"""