""" 
=> CPU Metircs
    
    -> All cpu queries from this metric 
       
       node_cpu_second_total
       
       THis is exposed by node exporter 
       
    -> Modes 
       
       1. Idle = doing nthng 
       2. users = running apps 
       3. system  = kernel works 
       4. iowait = waiting for disk


-------------------------------------------------------------------------------------

=> CPU doing nthng 
     
     100*(1 - avg(node_cpu_seconds_total{mode = "idle}[5m]))
     
     
     Across all CPUs (and instances), how much time per second the CPU was idle over the last 5 minutes.

=> Per instance CPU 
    
    100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode = "idle}[5m])
    ))                


=> Per core CPU 
   
   100 * (1- avg by (CPU) (rate(node_cpu_seconds_total{mode = "idle}[5m])))
   
   how much per code is idle
   
=> Per instance , core
            
            
            100 * (1 - avg by (instance, cpu) (
             rate(node_cpu_seconds_total{mode="idle"}[5m])
           ))   

=> Per mode 
    
    sum by (mode) (
    rate(node_cpu_seconds_total[5m])
    )
   
   Across all cpu , how much time per second is spent in each cpu mode

=> I/O wait 
             
             100 * avg(rate(node_cpu_seconds_total{mode="iowait"}[5m]))
             
             
=> CPU Load 
     
     node_load1
    
    Number of process waiting for cpu 


=> How much busy is each core 
    
    1. node_load1 
        
        1 min load average 
        
        no of process , running on cpu , waiting for cpu 
    
    2. count(node_cpu_seconds_total) by (cpu) 
         
         gets no of cpu core 
         
         count(count(node_cpu_second_total))
         
         total core 
    
    load / core 
    
    how much busy is each core

=> CPU satration 
     
     node_load1  > count(count(node_cpu_seconds_total) by (cpu))
     
     is the no of runnable / waiting process > no.of cpu cores 
     
     if true cpu is overloaded 

=> Max cpu at one point 
                        
                        
                        max_over_time(
                         100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[1m])))
                           [10m:]
                        ) > 90       
                        
                    Was CPU usage greater than 90% at any point in the last 10 minutes     


=> Top N busy instance 

         topk(3, 100 * (1 - avg by (instance) (
  rate(node_cpu_seconds_total{mode="idle"}[5m])
)))                                                    
"""