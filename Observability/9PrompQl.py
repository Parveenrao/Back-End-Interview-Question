"""  
=> Quantile 
     
     -> instead of average we ask ,  
        p90
        p95
        p99 
        
        p95 = 95 % of request are faster than this value

-----------------------------------------------------------------------------------

histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m]))     


---------------------------------------------------------------------------------------

-> histogram_quantile(
  0.95,
  sum(rate(request_duration_seconds_bucket[5m])) by (le)
)


   95% reqest are faster than this 
   
   only 5% request are slower , wrost we cn say
   

---------------------------------------------------------------------------------------------

histogram_quantile(0.95 , sum(rate(request_duration_seconds_bucket[5m])) by(le , endpoint))
   
   per end point latency   
   
   
     

"""