"""  
=> Network in Linux
    
    1. eth0 => main network
    2. lo => loopback (internal)
    3. docker 0 => containers
    
    Proemtheus expose metrics per interface 



-----------------------------------------------------------------------------------------------

=> node_network_recieve_bytes_total{device!~lo|docker.**}

    Remove lo (localhost traffic)
    docker.** (docker noise)


=> Network Throughput 
    
    1. Incoming traffic (bytes/sec)
        
        rate(node_network_recieve_bytes_total{device!~"lo|docker.**[5m]})
    
    2. Outgoing traffic 
        
        rate(node_network_transmit_bytes_total{device!~"lo|docker.*"}[5m])
    
    3. Total bandwidth 
    
          rate(node_network_receive_bytes_total[5m]) 
         + rate(node_network_transmit_bytes_total[5m])                
     
     
     High traffic ≠ problem
     Sudden spikes = suspicious
     Zero traffic = service down

----------------------------------------------------------------------------------------------

=> Packet rate 
     
     1. Packet recieved 
         
         rate(node_network_recieve_packets_total[5m])
     
     2. Packet sent 
         
         rate(node_network_transmit_packets_total[5m])


-------------------------------------------------------------------------------------------------

=> Errors 
    
    1. Recieve Errors
         
         rate(node_network_recieve_errs_total[5m])
    
    2.Transmit Erros 
        
        rate(node_network_transmit_errs_total[5m])
        
    3. ALert 
            
            rate(node_network_receive_errs_total[5m]) > 0


-----------------------------------------------------------------------------------------------------

=> Packet drops 
         
         rate(node_network_receive_drop_total[5m])



-------------------------------------------------------------------------------------------------------

=> Alert
       
       
       (
  rate(node_network_receive_errs_total[5m]) > 0
)
OR
(
  rate(node_network_receive_drop_total[5m]) > 0
)

-----------------------------------------------------------------------------------------------------

=> TOp busiest interface 
        
        
        
        topk(3,
     rate(node_network_receive_bytes_total[5m])
     )


---------------------------------------------------------------------------------------------------

=> Instance level filtering
           
           
    node_network_receive_bytes_total{
    instance="server-1:9100",
    device="eth0"
       }     
         
                     
                              
                  
     
"""