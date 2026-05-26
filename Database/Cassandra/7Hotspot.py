""" 
=> Hotspot Problem in Cassandra 
    
    A hotspot == too muhc traffic hitting the same node/partition
    
    -> One node overload 
    -> high latency
    -> Cluster look down 

------------------------------------------------------------------------------------------------

=> WHy hotspot happens 
      
      1. Bad Partition key 
          
          Primary key(country , user_id)
          
          if most user are from india , then all hit one node , and node will overload , become hotspot

-------------------------------------------------------------------------------------------------------

=> SOlution 
   
   1. Use High Cardinailty key (Unique values)
       
       Primary key (user_id) 
       
       millions of user -> evenly distributed
       
       
       primary key(status) , few values -> hotspot         
              


"""