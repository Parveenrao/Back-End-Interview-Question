""" 
=> How to Scale Prometheus 
  
  
  1. understand the limitation
      
      -> Prometheus is a 
          
          1. Single binary 
          2. Local storage (TSDB)
          3. No native clustering
  
  
  2. Vertical Scaling 
     
     -> Increase CPU , RAM 
     
     -> Faster disk (SSD , NVMe)
     
     -> Tune 
         
         scrape_interval
         retention
         num_samples
         
         work until millions of time series , then it breaks
   
   
   3. Horizontal Scaling using federation 
       
       -> Multiple Prometheus servers scrape different targets 
       
       -> A top level Prometheus aggregrates metrics 
       
                   [Prometheus A] --->\
                   [Prometheus B] ----> [Central Prometheus]
                   [Prometheus C] --->/     
   
   4. Functional Sharding
      
      -> Instead of scaling one prometheus , you split responsibilities
      
        Prometheus 1 -> Kubermetes metrics
        Prometheus 2 -> Database metrics
        Prometheus 3 -> App metrics
        
        Each handles fewer time series → better performance
   
   5. High availability setup 
       
       -> Run 2 prometheus instance scraping same target     
                                 


"""