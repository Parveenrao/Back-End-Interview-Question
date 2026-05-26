"""  
=> Self-Hosted-Runner 
    
    -> Is a machine you control (not github server) that runs your workflow
    
    -> Instead of 
        
        Githuh runner = Ubuntu-latest
        
    -> You use 
       
       Your own server EC2 , VM 

-----------------------------------------------------------------------------------

=> Why Self - Hosted Runners 
    
    1. Githuh Runner 
       -> Limited CPU/RAM
       
       -> Limited Runtime 
       
       No resource limit 
    
    2. Access to private infra
        
        -> Internal database
        -> Private kubernetes cluster 

-----------------------------------------------------------------------------
=> Working
   
   1. You created  a runner in github
   2. Github gives you a token 
   3. You install runner software on machine 
   4. Machine connect to GIthub
   5. JOb get assigned to it
 
 
 repo → Settings → Actions → Runners
-----------------------------------------------------------------------------

=> Workflows 
   
   jobs:
     build:
      runs-on : self-hosted 
      
      runs-on: [self-hosted, linux, gpu]

--------------------------------------------------------------------------------

=> Advance Concept 
    
    1. Emphemeral runner 
       
       -> Runner starts - Run jobs - destroyed 
          
          Secure and clean 
    
    2. Auto-Scaling runners 
         
         Spin up EC2 when job comes
         Shut down after 
    
    3. Docker inside runner 
       
       Runner -> build docker -deploys      
        
                               
                  

"""