""" 
=> Why Prometheus is not horizontally scalable 

   
   -> Prometheus is built as single-node system
       
       1. Open process
       2. One local disk 
       3. One TSDB
       
       IT 
       
       I scrape anything  , I store everything , I query everything

-------------------------------------------------------------------------------------------------------

=> No Native sharding 
     
     -> Prometheus does not split data across multiple node
     -> Each instance stores its own full dataset

=> No Distribute Engine 
     
     -> Queries run on one node only
     -> It doesn't aggregate result from multiple prometheus instance

=> Tight Coupling 

   -> In prometheus 
     
     Scraping + Storing  + Querying  = all in one instance
     
     you can't scale them independently


=> Local Storage Dependency 
    
    -> Uses local disk (TSDB)
    
    -> No shared / distributed storage by default

=> No built in Replication / HA
    
    -> No automatic data replication 
    
    -> No consenus System                          
       
       

"""