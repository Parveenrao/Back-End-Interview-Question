""" 
=> Disk space Basic Metrics 
     
     node_filesystem_size_bytes
     node_filesystem_free_bytes
     node_file_system_avail_bytes
     

------------------------------------------------------------------------------------------------------

=> Disk % Usage
    
    100 * (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes))
    
    show actual usable space 


=> Alert    , Disk almost full > 90%

   100 * (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) > 90
   
   
   free_bytes includes root reserved space
   avail_bytes = what your app can actually use    

------------------------------------------------------------------------------------------------

=> Disk I/O Performance Metrics
    
    1. Throughput = No of request handled 
    
        -> Read Throughput   
        
           rate(node_disk_read_bytes_total[5m])
        
        -> Write Throughput
           
           rate(node_disk_written_bytes_total[5m])
    
        -> Total Disk Throughput 
           
           rate(node_disk_read_bytes_total[5m]) + rate(node_disk_written_bytes_total[5m])
    
    
    2. IOPS (Operation per second)
        
        rate(node_disk_reads_completed_total[5m]) 
        
        rate(node_disk_write_completed_total[5m])
        
        
        High IOPS + latency == problem
    
    
    3. Latency 
        
        -> Read latency 
        
            rate(node_disk_read_time_seconds_total[5m]) 
            / rate(node_disk_reads_completed_total[5m])                  
        
        -> write latency 
            
            rate(node_disk_write_time_seconds_total[5m]) 
            / rate(node_disk_writes_completed_total[5m])  
        
        
        -> Alert 
                    
                    (
              rate(node_disk_read_time_seconds_total[5m]) 
                / rate(node_disk_reads_completed_total[5m])
               ) > 0.05      
    
    4. Disk utilization 
        
        -> IS disk saturated 
        
           rate(node_disk_io_time_seconds_total[5m])   = disk busy %
        
        
        -> rate(node_disk_io_time_seconds_total[5m]) > 0.9
    
    5. Queue length 
    
            rate(node_disk_io_time_weighted_seconds_total[5m])
            
            High  = request waiting slow system

-------------------------------------------------------------------------------------------------

=> Per instance disk usage 
                     
             avg by (instance) (
         100 * (1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes))
          )


-----------------------------------------------------------------------------------------

=> Filters in Disk 
    
    1. fake device 
        
        device !~"loop|ram"
    
    2. File system filter 
        
        fstype!="tmfps 
        
        tmfps = memory , not disk
    
    3. mountpoint 
       
       mountpoint!~"/run|/proc|/sys"          
    
    
    4. Real query
           
           
           
           100 * (
            1 - (
         node_filesystem_avail_bytes{
          fstype!="tmpfs",
         mountpoint!~"/run|/proc|/sys"
             }
              /
           node_filesystem_size_bytes{
          fstype!="tmpfs",
          mountpoint!~"/run|/proc|/sys"
          }
        )
       )           
                                        

"""