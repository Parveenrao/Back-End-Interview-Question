""" 
=> Availability Zone(AZ)
    
    -> a separate physical data centre (or group of centre) inside a region
    
    -> Each EZ 
       1. has its own power , cooling , networking 
       2. is isolated from failure
       3. is connected to other AZ with fast private network


-------------------------------------------------------------------------------------------

=> Example 
   
   Region = City 
   AZ = different buildings in city
   
   if one buildings burn 
   other still work


--------------------------------------------------------------------------------------------

=> WHy AZs
   
   1. Fault tolerant 
      
      -> if one AZ fail = your app not go down
   
   2. High availability 
       
       -> Run our server in multiple AZ
          
          EC2  in AZ-a
          EC2  in AZ-b
          
          if AZ-a crash , traffic goes to AZ-b
    
    3. Low latency 
       
       -> Azs are connected with high -speed links
           1. fast Db replication 
           2.fast service communication
    
    
    
            Load Balancer
           /             \
     EC2 (AZ-a)     EC2 (AZ-b)
           \             /
           RDS (Multi-AZ)                          

"""