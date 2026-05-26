""" 
=> Group_left / Group_right
   
   -> Normally proemtheus expect a 1:1 match between time series
   
     metric A * metrix B
     
     -> But in real system it is 1:N  , N:1
     
     -> Example   
        
        
        http_total_request = labels : {instacen , job}
        
        we want to join on instance 
        
        one side has extra label , and side have more series

----------------------------------------------------------------------------------------------

1. Group left 
    
    Many -> One , keep left side
    
    -> left side has more series
    -> Right side has more series
    
    http_requests_total * on(instance) group_left(region) instance_info
    
    Match on instance
    Left side (http_requests_total) has many series
    Right side (instance_info) has fewer
    Add region label from right → into result        
    
    Result will keep left side cardinality, but enrich it with labels from right.

2. Group Right
    
    One -> Many 
    
    Right side has more series
    Left side has fewer series
    You want to keep labels from left side
    
    
    cpu_usage * on(instance) group_right(role) machine_role
    
------------------------------------------------------------------------------------

=> Real Interview

  1. rate(http_request_total[5m])
  
     instance_info{region="us-east"}
  
      -> you want request         
      
      
      rate(http_requests_total[5m])
         * on(instance)
          group_left(region)
          instance_info    

"""