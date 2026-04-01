"""

=> Monolithic Architecture 
   
   -> A monolithic architecture is a system where all component (UI , busniess logic , data access) are built , deployed 
      and run as a single unit
   
   -> Everything live together 
        1. One codebase
        2. One Deployment
        3. One Runtime
    
   -> Example 
      1. User login 
      2. Product listing
      3. payment 
      4. Orders 
      
      All modules → inside ONE application
      
      No separate services 
----------------------------------------------------------------------------------------------------------------------     

=> Structure of Microservices 
   
   1. Presentation Layer 
      -> Controllers / API
   
   2. Business Logic Layer 
      
      -> workflow and rules 
   
   3. Data Access Layer 
       
       -> Sql queries
   
   5. Database 
      
      -> Usually one shared  db
      
--------------------------------------------------------------------------------------------------------------------------

=> Working 
   
   1. Request come to server 
   2. Controller handles it 
   3. Business logic executes it 
   4. Db accessed 
   5. Response return 
   
   All inside same process

-----------------------------------------------------------------------------------------------------------------------------

=> Pros 
    
    1. Simplicity 
        -> Easy to build
        -> Easy to understand 
    
    2. Faster Development 
       -> No network calls 
       -> No distributed complexity 
    
    3. Better Performance 
       
       -> No-inter-service latency

-----------------------------------------------------------------------------------------------------------------------------
=> Disadvantage 
   
   1. Tight Coupling         
       -> Change in one module can break others 
   
   2. Scalability issue 
      
      -> We scale whole app , not one service 
       
       Example  ---> Payment Service is heavy , but we scale whole app
   
   3. Slow Deployment 
       
       -> Small change --> redeploy entire app       
   
   4. Tech-lock In 
       
       -> One language , framework for everything

---------------------------------------------------------------------------------------------------------------------------------

=> Types of Monolithis
    
    1. Traditional Monolith
       -> Everything tight coupled
    
    2. Modular Monolith
        
        -> Code is divided into modules
        
        -> But still one deployable 

------------------------------------------------------------------------------------------------------------------------------

=> Anti Pattern In Monoliths 
  
  1. Big Ball Of Mud
      -> No structure 
  
  2. Shared Database
     
     -> Everyone touch everything 
  
  3. Tight Coupling

----------------------------------------------------------------------------------------------------------------------------

=> Scaling Monolithic 
    
    -> First Principle 
        Scaling a monolithic means , scaling entire application  , not individual component
    
    1. Vertical Scaling (Scale Up)
       ->  Increase machine power (CPU , RAM , DISK)
       
       -> Single Point Of Failure 
       -> Hardware limit 
       -> Expensive 
    
    2. Horizontal Scaling 
        
        Load Balancer
        /    |    \
      App1   App2   App3      
      
      -> Run multiple instance of app behind lb , 
       
      -> Still scaling enitre app 
   
   3. Modular Scaling 
       -> Indentify hotspot 
        
        use async processing '
        
   4. DataBase Scaling 
      
      In real system , database dies before application does 
      
      1. Read Replica 
         -> Write primary db 
         -> Read , replica 
      
      2. Caching 
         -> Reduce DB hit ,
             Redis , Memcached
      
      3. Connection Pooling 
         -> Reduce DB overload
      
      4. Sharding 

--------------------------------------------------------------------------------------------------------------------------

=> Breaking Monolithic Into MicroService 
   
First Principle 
   -> We dont break a monolithic all at once , we extract services based on busniess boundaries 
    
    1. Understand Monolithic 
       
        Identify 
        
        Modules , Dependencies , Database usage , Hotspot 
    
    2. Indentify Bounded Context (DDD)
       
       User Management 
       Order System
       Payment System
       Inventory 
       
       Each become candidate service 
       
       High cohesion inside 
       Low coupling outside
    
    3. Start with Right Service 
       
       -> Dont start with Tight Coupled Service 
       
       -> Start with Low Dependency modules 
           
           Auth Service , Notification Service 
    
    4. Strangler Fig Pattern
    
                    Client
                      ↓
               Proxy / API Gateway
                  ↓        ↓
              Monolith   New Service  
              
              Gradually route traffic to new services
               Old system slowly “dies”              
    
    5. Extract Services 
       
       1. Copy logic from monolith
       2. Create independent service 
       3 Expose API
    
    6. Replace Internall calls with APIs
       
       In monolithic , there is function calls 
       
       In microservice  HTTP/grpc calls
       
      -> Problem introduced   
         1. Network latency 
         2. Failure
                                 
    7. Handle Distributed Challenges 
       
       1. Network Failures 
          -> Timeout 
          -> Retry 
       
       2. Data consistency 
           -> Use eventual consistency
           -> Saga pattern 
    
    => Example 
    
       1. Extract Notification Service
       2. Extract Auth Service
       3. Extract order Service 
       4. Introduce Event-Driven-Architecture 



----------------------------------------------------------------------------------------------------------------

=> How Monolithic Communicate 
   
   -> Function call
   -> Method call
   -> Shared Memory                                                                                                         

"""